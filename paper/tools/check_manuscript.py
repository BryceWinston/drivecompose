"""Check the current experiment contract, archives, dependencies and bilingual math."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


# Preserve evidence paths when current figures are renamed and old files archived.
def figure_asset(name: str | Path) -> Path:
    path = Path(name)
    value = str(path).replace("\\", "/")
    if "/drivecompose/" in value:
        relative = value.split("/drivecompose/", 1)[1]
    elif value.startswith(("paper/", "docs/")):
        relative = value
    elif value.startswith("fig/"):
        relative = "paper/" + value
    else:
        return path
    current = ROOT.parent / relative
    if current.is_file():
        return current
    layout_path = ROOT / "provenance/figure-layout.json"
    if layout_path.is_file():
        layout = json.loads(layout_path.read_text(encoding="utf-8"))
        roots = layout.get("historical_asset_roots_relative_to_project", [
            layout["archive_root_relative_to_project"] + "/files"
        ])
        for archive in roots:
            historical = ROOT.parent / archive / relative
            if historical.is_file():
                return historical
    return current


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def uncomment(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def document(main: str, folder: str) -> str:
    return uncomment((ROOT / main).read_text(encoding="utf-8")) + "\n" + "\n".join(
        uncomment(p.read_text(encoding="utf-8")) for p in sorted((ROOT / folder).glob("*.tex"))
    )


def math_blocks(name: str) -> list[str]:
    text = uncomment((ROOT / name).read_text(encoding="utf-8"))
    blocks = re.findall(r"\\begin\{(equation|align)\}(.*?)\\end\{\1\}", text, re.S)
    return [
        re.sub(r"\s+", "", re.sub(r"\\label\{[^}]+\}", "", body)).rstrip(",.")
        for _, body in blocks
    ]


def ablation_source(source: str) -> str:
    """Select the ablation protocol and its analyses, excluding other experiments."""
    marker = source.find(r"\label{sec:ablation-protocol}")
    if marker < 0:
        return ""
    start = source.rfind(r"\subsection{", 0, marker)
    return source[start:] if start >= 0 else ""


def blank_ablation_tables(source: str) -> tuple[bool, bool]:
    """Allow variant IDs/input counts, but require every result cell to be empty."""
    tables = re.findall(r"\\begin\{table\}(.*?)\\end\{table\}", source, re.S)
    if len(tables) != 2:
        return False, False
    expected_ids = (["A0", "A1", "A2", "A3", "A7"],
                    ["A0", "A2", "A0", "A2", "A0", "A2"])
    results = []
    for index, table in enumerate(tables):
        body = re.search(r"\\midrule(.*?)\\bottomrule", table, re.S)
        if body is None:
            results.append(False)
            continue
        rows = [[cell.strip() for cell in row.strip().split("&")]
                for row in re.split(r"\\\\", body.group(1)) if row.strip()]
        ids = [re.search(r"\((A\d+)\)", row[0]) for row in rows]
        valid = (all(ids) and [match.group(1) for match in ids] == expected_ids[index]
                 and all(len(row) == 5 for row in rows))
        if index == 0:
            valid = valid and all(not cell for row in rows for cell in row[1:])
        else:
            valid = (valid and [row[1] for row in rows] == ["2", "2", "4", "4", "8", "8"]
                     and all(not cell for row in rows for cell in row[2:]))
        results.append(bool(valid))
    return results[0], results[1]


def reported_ablation_tables(source: str, record: dict,
                             displayed_component_columns: list[str] | None = None) -> dict[str, bool]:
    """Compare result cells (including blanks), variant names and input counts."""
    tables = re.findall(r"\\begin\{table\*?\}(.*?)\\end\{table\*?\}", source, re.S)
    labels = {
        label: ("tab:seed-inputs" if label == "tab:ablation-inputs"
                and r"\label{tab:ablation-inputs}" not in source
                and r"\label{tab:seed-inputs}" in source else label)
        for label in record["tables"]
    }
    selected = [table for table in tables
                if any(r"\label{" + label + "}" in table for label in labels.values())]
    checks = {"ablation_table_count": len(selected) == len(record["tables"])}
    parsed = {}
    for label, expected in record["tables"].items():
        expected_rows = expected["rows"]
        if label == "tab:ablation-components" and displayed_component_columns is not None:
            indices = [expected["columns"].index(column)
                       for column in displayed_component_columns]
            expected_rows = [[row[index] for index in indices] for row in expected_rows]
        matches = [table for table in selected if "\\label{" + labels[label] + "}" in table]
        rows = []
        if len(matches) == 1:
            body = re.search(r"\\midrule(.*?)\\bottomrule", matches[0], re.S)
            if body:
                grouped_body = re.sub(r"\\midrule", "", body.group(1))
                input_t = None
                for row in re.split(r"\\\\", grouped_body):
                    if not row.strip():
                        continue
                    cells = [re.sub(r"\\textbf\{([^{}]+)\}", r"\1", cell.strip())
                             for cell in row.split("&")]
                    cells = [re.sub(r"\\multirow\{2\}\{\*\}\{([^{}]+)\}", r"\1", cell)
                             for cell in cells]
                    cells = ["-" if cell == "--" else cell for cell in cells]
                    if labels[label] == "tab:seed-inputs":
                        cells = [re.split(r"\s*\$\\pm\$", cell, maxsplit=1)[0].strip()
                                 for cell in cells]
                    if label == "tab:ablation-inputs" and len(cells) == 5:
                        input_t = cells[0] or input_t
                        cells = [cells[1], input_t, *cells[2:]]
                    rows.append(cells)
        parsed[label] = rows
        checks[label + ":expected_cells_exact"] = rows == expected_rows
    component_columns = (displayed_component_columns
                         or record["tables"]["tab:ablation-components"]["columns"])
    input_columns = record["tables"]["tab:ablation-inputs"]["columns"]
    shared_metrics = [column for column in input_columns[2:] if column in component_columns]
    components = {row[0]: row for row in parsed.get("tab:ablation-components", [])
                  if len(row) == len(component_columns)}
    t8 = [row for row in parsed.get("tab:ablation-inputs", [])
          if len(row) == 5 and row[1] == "8"]
    checks["ablation_t8_consistent"] = (
        len(t8) == 2 and {row[0] for row in t8} == {"Ours", "w/o CCM"}
        and bool(shared_metrics)
        and all(row[0] in components and all(
            row[input_columns.index(metric)] == components[row[0]][component_columns.index(metric)]
            for metric in shared_metrics) for row in t8)
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-root", type=Path,
                        help="External cleanup archive; defaults to provenance/archive-map.json.")
    args = parser.parse_args()
    provenance = ROOT / "provenance"
    revision_path = provenance / "review-revision-20261030.json"
    revised_layout = revision_path.is_file()
    manifest_path = provenance / "source-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    archive_map = json.loads((provenance / "archive-map.json").read_text(encoding="utf-8"))
    archive_root = (args.archive_root or
                    ROOT.parent / archive_map["archive_root_relative_to_project"]).resolve()
    if not archive_root.is_dir():
        parser.error(f"External archive not found: {archive_root}. Use --archive-root PATH.")
    checks: dict[str, bool] = {}
    details: dict[str, object] = {"archive_root": str(archive_root)}
    checks["migration_manifest_unchanged"] = digest(manifest_path.read_bytes()) == archive_map["source_manifest_sha256"]
    moves_path = archive_root / archive_map["moves_manifest"]
    checks["archive_moves_manifest_unchanged"] = digest(moves_path.read_bytes()) == archive_map["moves_manifest_sha256"]
    moves = json.loads(moves_path.read_text(encoding="utf-8"))["files"]
    invalid_archive_files = [item["destination"] for item in moves
                             if not (archive_root / item["destination"]).is_file()
                             or digest((archive_root / item["destination"]).read_bytes()) != item["sha256"]]
    checks["archived_files_exact"] = not invalid_archive_files
    details["invalid_archive_files"] = invalid_archive_files
    details["archived_file_count"] = len(moves)
    archive_path = archive_root / archive_map["original_manuscript_zip"]
    checks["archive_copy_exact"] = digest(archive_path.read_bytes()) == manifest["source_zip_sha256"]
    empty_record = json.loads((provenance / "experiments-empty-20261021.json").read_text(encoding="utf-8"))
    framework_path = provenance / "ablation-framework-20261021.json"
    framework_record = (json.loads(framework_path.read_text(encoding="utf-8"))
                        if framework_path.is_file() else None)
    results_path = provenance / "ablation-results-20261023.json"
    standard_metrics_path = provenance / "ablation-standard-metrics-20261029.json"
    if standard_metrics_path.is_file():
        results_path = standard_metrics_path
    results_record = (json.loads(results_path.read_text(encoding="utf-8"))
                      if results_path.is_file() else None)
    presentation_path = provenance / "core-ablation-revision-20261104.json"
    presentation_record = (json.loads(presentation_path.read_text(encoding="utf-8"))
                           if presentation_path.is_file() else None)
    component_figure_path = provenance / "component-ablation-figure-20261105.json"
    component_figure_record = (json.loads(component_figure_path.read_text(encoding="utf-8"))
                               if component_figure_path.is_file() else None)
    if component_figure_record:
        for kind in ("pdf", "svg"):
            asset = ROOT / component_figure_record[kind]
            checks[f"component_ablation:{kind}_matches_record"] = (
                asset.is_file()
                and digest(asset.read_bytes()) == component_figure_record[kind + "_sha256"]
            )
        source_dir = ROOT / component_figure_record["source_dir"]
        checks["component_ablation:source_images_exact"] = all(
            (source_dir / item["file"]).is_file()
            and digest((source_dir / item["file"]).read_bytes()) == item["sha256"]
            for item in component_figure_record["sources"]
        )
    frozen = [
        "cvpr.sty", "lineno.sty",
        "ieeenat_fullname.bst", "preamble.tex",
    ]
    with zipfile.ZipFile(archive_path) as archive:
        frozen_hashes = {}
        for name in manifest["frozen_experiments"]:
            backup = Path(empty_record["files"][name]["previous_source_backup"])
            checks["archived_original:" + name] = (
                backup.is_file() and digest(backup.read_bytes()) == digest(archive.read(name))
            )
        for name in frozen:
            actual, original = digest((ROOT / name).read_bytes()), digest(archive.read(name))
            style_record = provenance / "author-results-followup-20261030.json"
            if name == "cvpr.sty" and style_record.is_file():
                official_style = json.loads(style_record.read_text(encoding="utf-8"))["official_template"]["style_sha256"]
                checks["official2027:cvpr.sty"] = actual == official_style
                checks["official2027:supplementary/cvpr.sty"] = digest((ROOT / "supplementary/cvpr.sty").read_bytes()) == official_style
            else:
                checks["unchanged:" + name] = actual == original
            frozen_hashes[name] = {"sha256": actual, "original_sha256": original}
    details["frozen_hashes"] = frozen_hashes
    details["source_git_commit"] = manifest["source_git_commit"]

    overview_source = archive_root / archive_map["overview_original"]
    historical_overview = (ROOT.parent / archive_map.get(
        "overview_copy_relative_to_project", "paper/fig/drivecompose-overview.png"
    )).resolve()
    checks["overview_copy_exact"] = (
        historical_overview.is_file()
        and digest(historical_overview.read_bytes()) == digest(overview_source.read_bytes())
    )
    details["historical_overview_copy"] = str(historical_overview)
    details["raster_overview_role"] = "historical design draft; current entries use author-selected mechanism illustrations"
    selection_path = provenance / "figure-replacement-20261104.json"
    selection = (json.loads(selection_path.read_text(encoding="utf-8"))
                 if selection_path.is_file() else None)
    layout_path = provenance / "figure-layout.json"
    layout = (json.loads(layout_path.read_text(encoding="utf-8"))
              if layout_path.is_file() else None)
    layout_figures = {figure["label"]: figure for figure in layout["figures"]} if layout else {}
    overview_filename = (Path(layout_figures["fig:overview"]["pdf"]).name
                         if "fig:overview" in layout_figures else
                         (Path(selection["figures"]["fig:overview"]["active_path"]).name
                          if selection else "drivecompose-inference-overview.png"))
    overview = ROOT / "fig" / overview_filename
    checks["generated_overview_exists"] = overview.is_file()
    mechanism_raster_records = sorted(provenance.glob("mechanism-image-replacement-*.json"))
    mechanism_filename = (Path(layout_figures["fig:joint-completion"]["pdf"]).name
                          if "fig:joint-completion" in layout_figures else
                          (Path(selection["figures"]["fig:joint-completion"]["active_path"]).name
                           if selection else ("drivecompose-joint-completion.png" if mechanism_raster_records
                                              else "drivecompose-joint-completion.pdf")))
    if selection:
        details["active_figure_selection"] = str(selection_path.relative_to(ROOT))
        for label, figure in selection["figures"].items():
            active = (ROOT.parent / layout_figures[label]["pdf"]
                      if label in layout_figures else figure_asset(ROOT.parent / figure["active_path"]))
            checks[label + ":active_export_matches_record"] = (
                active.is_file() and digest(active.read_bytes()) == figure["sha256"]
            )
            if "native_source" in figure:
                native = figure_asset(ROOT.parent / figure["native_source"])
                checks[label + ":editable_source_matches_record"] = (
                    native.is_file() and digest(native.read_bytes()) == figure["native_sha256"]
                )
    for entry in ("main.tex", "main_zh.tex"):
        source = uncomment((ROOT / entry).read_text(encoding="utf-8"))
        if revised_layout:
            supplement = "evaluation_zh.tex" if entry == "main_zh.tex" else "evaluation.tex"
            supplement_text = uncomment((ROOT / "supplementary" / supplement).read_text(encoding="utf-8"))
            method = "zh/3_method_zh.tex" if entry == "main_zh.tex" else "sec/3_method.tex"
            method_text = uncomment((ROOT / method).read_text(encoding="utf-8"))
            # A double-column float can be queued before Related Work so that
            # it opens the Method page. Its asset and label must remain unique.
            introduction = "zh/1_introduction_zh" if entry == "main_zh.tex" else "sec/1_introduction"
            related = "zh/2_related_work_zh" if entry == "main_zh.tex" else "sec/2_related_work"
            overview_sources = source + method_text
            queued_before_method = (
                r"\label{fig:overview}" in source
                and source.index(r"\input{" + introduction + "}")
                < source.index(r"\label{fig:overview}")
                < source.index(r"\input{" + related + "}")
            )
            checks[entry + ":overview_queued_once_for_method"] = (
                overview_sources.count("{fig/" + overview_filename + "}") == 1
                and overview_sources.count(r"\label{fig:overview}") == 1
                and r"\ref{fig:overview}" in method_text
                and (queued_before_method or r"\label{fig:overview}" in method_text)
            )
            checks[entry + ":mechanism_selected_asset_in_main_only"] = (
                method_text.count("{fig/" + mechanism_filename + "}") == 1
                and "drivecompose-joint-completion" not in supplement_text
                and Path(mechanism_filename).stem not in supplement_text
                and r"\label{fig:supp-detail}" not in supplement_text
            )
            checks[entry + ":llm_usage_statement_active"] = (
                "7_llm_usage" in source
                and source.index("7_llm_usage") < source.index(r"\bibliography")
            )
        else:
            checks[entry + ":generated_overview_active"] = (
                (r"\includegraphics[width=\textwidth]{fig/" + overview_filename + "}") in source
                and "drivecompose-overview.png" not in source
            )
    figure_record_path = provenance / "three-figure-integration-20261029.json"
    if figure_record_path.exists():
        figure_record = json.loads(figure_record_path.read_text(encoding="utf-8"))
        for language, entry, folder in (("en", "main.tex", "sec"), ("zh", "main_zh.tex", "zh")):
            text = document(entry, folder)
            for figure in figure_record["figures"]:
                path = figure_asset(figure["path"])
                name = "fig/" + path.name
                if not revised_layout:
                    checks[f"{language}:figure{figure['number']}_active"] = (
                        text.count("{" + name + "}") == 1
                        and text.count("\\label{" + figure["label"] + "}") == 1
                    )
                expected_sha = figure["sha256"]
                # Later author-selected exports supersede the initial overview.
                if figure.get("label") == "fig:overview":
                    replacements = sorted(provenance.glob("overview-pdf-replacement-*.json"))
                    if replacements:
                        replacement = json.loads(replacements[-1].read_text(encoding="utf-8"))
                        approved = figure_asset(ROOT.parent / replacement["active_png"])
                        if approved.resolve() == path.resolve():
                            expected_sha = replacement["png_sha256"]
                if figure.get("label") == "fig:joint-completion":
                    replacements = mechanism_raster_records or sorted(
                        provenance.glob("mechanism-vector-replacement-*.json")
                    )
                    if replacements:
                        replacement = json.loads(replacements[-1].read_text(encoding="utf-8"))
                        approved = figure_asset(ROOT.parent / replacement["active_png"])
                        if approved.resolve() == path.resolve():
                            expected_sha = replacement["png_sha256"]
                        if mechanism_raster_records:
                            checks["mechanism_author_selected_image_exact"] = (
                                approved.is_file()
                                and digest(approved.read_bytes()) == replacement["source_sha256"]
                            )
                        else:
                            vector = figure_asset(ROOT.parent / replacement["active_pdf"])
                            native = figure_asset(ROOT.parent / replacement["native_source"])
                            checks["mechanism_vector_export_matches_record"] = (
                                vector.is_file()
                                and digest(vector.read_bytes()) == replacement["pdf_sha256"]
                                and native.is_file()
                                and digest(native.read_bytes()) == replacement["native_sha256"]
                            )
                checks[f"figure{figure['number']}_approved_pixels_exact"] = (
                    path.is_file() and digest(path.read_bytes()) == expected_sha
                )
            if revised_layout:
                current_figures = {
                    "fig01-teaser.pdf": "fig:teaser",
                    overview_filename: "fig:overview",
                    mechanism_filename: "fig:joint-completion",
                    "fig04-dynamic-reconstruction.pdf": "fig:dynamic-reconstruction",
                    "fig05-off-trajectory-rendering.pdf": "fig:waymo-left-shift",
                }
                if component_figure_record:
                    current_figures[Path(component_figure_record["pdf"]).name] = "fig:component-ablation"
                for name, label in current_figures.items():
                    checks[f"{language}:{label}:active_once"] = (
                        text.count("{fig/" + name + "}") == 1
                        and text.count(r"\label{" + label + "}") == 1
                    )
    for language, name, heading in (("en", "sec/4_experiments.tex", "Experiments"),
                                     ("zh", "zh/4_experiments_zh.tex", "实验")):
        source = uncomment((ROOT / name).read_text(encoding="utf-8")).strip()
        if framework_record:
            required = ["sec:experiments", "sec:ablation-protocol", "sec:ablation-studies",
                        "sec:ablation-reuse", "tab:ablation-components", "tab:ablation-inputs"]
            if revised_layout and not presentation_record:
                required.remove("tab:ablation-inputs")
            empty_image_slots = results_record["empty_image_slots"] if results_record else 16
            if empty_image_slots:
                required.append("fig:ablation-reuse")
            checks[language + ":ablation_structure"] = (
                source.startswith("\\section{" + heading + "}")
                and all(source.count("\\label{" + label + "}") == 1 for label in required)
            )
            scoped_source = ablation_source(source)
            table_source = scoped_source
            if revised_layout:
                supplement = "evaluation_zh.tex" if language == "zh" else "evaluation.tex"
                table_source += "\n" + uncomment(
                    (ROOT / "supplementary" / supplement).read_text(encoding="utf-8"))
            if results_record:
                checks.update({language + ":" + key: value for key, value in
                               reported_ablation_tables(
                                   table_source, results_record,
                                   presentation_record["component_columns"]
                                   if presentation_record else None).items()})
                if presentation_record:
                    main_tables = re.findall(
                        r"\\begin\{table\*?\}(.*?)\\end\{table\*?\}", scoped_source, re.S)
                    checks[language + ":two_core_ablation_tables_in_main"] = (
                        len(main_tables) == 2
                        and all(any(r"\label{" + label + "}" in body for body in main_tables)
                                for label in presentation_record["main_tables"]))
                if results_path == standard_metrics_path:
                    checks[language + ":standard_ablation_metrics"] = all(
                        metric in scoped_source for metric in ("PSNR", "SSIM", "LPIPS"))
                    ablation_metric_tables = "\n".join(
                        body for body in re.findall(
                            r"\\begin\{table\*?\}(.*?)\\end\{table\*?\}",
                            scoped_source, re.S)
                        if any(r"\label{" + label + "}" in body
                               for label in ("tab:ablation-components", "tab:ablation-inputs"))
                    )
                    checks[language + ":custom_ablation_metrics_removed"] = (
                        not re.search(r"New-MAE|NVS-MAE|Obs-Reg|eq:regression", scoped_source)
                        and not re.search(r"Cov\.|\bPass\b", ablation_metric_tables)
                    )
                else:
                    checks[language + ":ablation_error_scale_explicit"] = (
                        r"$[0,1]$" in scoped_source and "RGB" in scoped_source
                    )
                checks[language + ":ablation_names_without_ids"] = not re.search(
                    r"\bA\d+\b", scoped_source
                )
            else:
                components_empty, inputs_empty = blank_ablation_tables(scoped_source)
                checks[language + ":component_results_blank"] = components_empty
                checks[language + ":input_results_blank"] = inputs_empty
            if empty_image_slots:
                checks[language + ":ablation_images_blank"] = (
                    scoped_source.count(r"\begin{figure*}") == 1
                    and scoped_source.count(r"\dcablationcell{") == empty_image_slots
                    and r"\includegraphics" not in scoped_source
                    and r"\fbox{\rule{0pt}{#2}\rule{.90\linewidth}{0pt}}" in scoped_source
                )
            elif component_figure_record:
                component_figures = [body for body in re.findall(
                    r"\\begin\{figure\}(.*?)\\end\{figure\}", scoped_source, re.S)
                    if r"\label{fig:component-ablation}" in body]
                checks[language + ":component_ablation_single_column"] = (
                    len(component_figures) == 1
                    and r"\includegraphics[width=\linewidth]{" + component_figure_record["pdf"] + "}" in component_figures[0]
                    and r"\ref{fig:component-ablation}" in scoped_source
                    and r"\begin{figure*}" not in scoped_source
                    and r"\dcablationcell" not in scoped_source
                )
            else:
                checks[language + ":ablation_figure_removed"] = all(
                    token not in scoped_source for token in
                    ("fig:ablation-reuse", r"\begin{figure", r"\dcablationcell", r"\includegraphics")
                )
        else:
            expected = "\\section{" + heading + "}\n\\label{sec:experiments}"
            checks[language + ":experiments_empty"] = source == expected
    checks["no_experiment_figure_addendum"] = (
        not (ROOT / "sec/4_reference_figures.tex").exists()
        and "4_reference_figures" not in uncomment((ROOT / "main.tex").read_text(encoding="utf-8"))
    )
    details["experiment_state"] = (results_record or framework_record or empty_record)["active_state"]
    source_hashes = manifest["current_sources_sha256"]
    historical_copies = archive_map["historical_source_copies"]
    missing_source_evidence = []
    changed_sources = []
    for name, sha in source_hashes.items():
        evidence = (archive_root / historical_copies[name] if name in historical_copies
                    else ROOT.parent / name)
        if not evidence.is_file() or digest(evidence.read_bytes()) != sha:
            missing_source_evidence.append(name)
        current = ROOT.parent / name
        if not current.is_file() or digest(current.read_bytes()) != sha:
            changed_sources.append(name)
    checks["migration_source_snapshot_preserved"] = not missing_source_evidence
    details["invalid_migration_source_evidence"] = missing_source_evidence
    details["changed_project_sources_since_migration"] = changed_sources
    details["historical_source_copies"] = historical_copies

    bib = (ROOT / "main.bib").read_text(encoding="utf-8")
    keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)", bib)
    checks["unique_bibliography_keys"] = len(keys) == len(set(keys))
    used = set()
    for language, entry, folder in (("en", "main.tex", "sec"), ("zh", "main_zh.tex", "zh")):
        text = document(entry, folder)
        year = re.findall(r"\\def\\confYear\{([^}]+)\}", text)
        checks[language + ":cvpr2027"] = year == ["2027"]
        cites = {key.strip() for group in re.findall(r"\\cite\w*\{([^}]+)\}", text) for key in group.split(",")}
        used |= cites
        missing = sorted(cites - set(keys))
        checks[language + ":resolved_citations"] = not missing
        details[language + ":missing_citations"] = missing
        labels = re.findall(r"\\label\{([^}]+)\}", text)
        refs = re.findall(r"\\(?:ref|eqref|cref|Cref)\{([^}]+)\}", text)
        checks[language + ":unique_labels"] = len(labels) == len(set(labels))
        checks[language + ":resolved_references"] = not (set(refs) - set(labels))
        missing_files = []
        for kind, name in re.findall(r"\\(input|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}", text):
            target = ROOT / (name + ".tex" if kind == "input" and not Path(name).suffix else name)
            if not target.is_file():
                missing_files.append(name)
        checks[language + ":resolved_files"] = not missing_files
        details[language + ":missing_files"] = missing_files
        rewritten = "\n".join(
            p.read_text(encoding="utf-8") for p in (ROOT / folder).glob("*.tex") if not p.name.startswith("4_")
        )
        checks[language + ":new_prose_has_no_old_modules"] = not re.search(r"MOSAIC|CamViT|MVDiT|DA3|13\.5", rewritten)

    checks["active_bibliography_has_no_unused_entries"] = used == set(keys)
    en_math, zh_math = math_blocks("sec/3_method.tex"), math_blocks("zh/3_method_zh.tex")
    checks["bilingual_method_math_identical"] = en_math == zh_math and bool(en_math)
    inline_math = []
    for name in ("sec/3_method.tex", "zh/3_method_zh.tex"):
        source = uncomment((ROOT / name).read_text(encoding="utf-8"))
        inline_math.append(sorted(re.sub(r"\s+", "", part) for part in
                                  re.findall(r"(?<!\\)\$(.*?)(?<!\\)\$", source, re.S)))
    checks["bilingual_method_inline_math_identical"] = inline_math[0] == inline_math[1]
    details["displayed_method_math_blocks"] = {"en": len(en_math), "zh": len(zh_math)}
    details["bibliography_entries"] = len(keys)
    details["bilingual_experiments_intentionally_empty"] = not bool(framework_record)
    if framework_record:
        experiment_math = []
        for name in ("sec/4_experiments.tex", "zh/4_experiments_zh.tex"):
            source = ablation_source(uncomment((ROOT / name).read_text(encoding="utf-8")))
            experiment_math.append(sorted(re.sub(r"\s+", "", part) for part in
                                          re.findall(r"(?<!\\)\$(.*?)(?<!\\)\$", source, re.S)))
        checks["bilingual_ablation_inline_math_identical"] = experiment_math[0] == experiment_math[1]
        results_blank = not results_record or results_record.get("result_state") == "blank"
        details["ablation_results_and_images_blank"] = results_blank
        details["ablation_results_filled"] = not results_blank
        details["ablation_images_blank"] = bool(
            results_record["empty_image_slots"] if results_record else 16
        )
        details["ablation_figure_removed"] = bool(
            results_record and results_record.get("ablation_figure_removed")
            and not component_figure_record
        )
        if component_figure_record:
            details["qualitative_component_ablation_record"] = str(component_figure_path.relative_to(ROOT))
        details["experiment_contract"] = str(
            (results_path if results_record else framework_path).relative_to(ROOT))
    details["checks"] = checks
    details["passed"] = all(checks.values())
    target = ROOT / "build/verification.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(details, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failed = [name for name, passed in checks.items() if not passed]
    print(json.dumps({"passed": not failed, "checks": len(checks), "failed": failed,
                      "bibliography_entries": len(keys), "math_blocks": len(en_math)}, ensure_ascii=True))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
