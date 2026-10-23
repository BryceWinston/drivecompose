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


def reported_ablation_tables(source: str, record: dict) -> dict[str, bool]:
    """Compare each retained result, variant name and input count at recorded precision."""
    tables = re.findall(r"\\begin\{table\}(.*?)\\end\{table\}", source, re.S)
    checks = {"ablation_table_count": len(tables) == len(record["tables"])}
    parsed = {}
    for label, expected in record["tables"].items():
        matches = [table for table in tables if "\\label{" + label + "}" in table]
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
                    if label == "tab:ablation-inputs" and len(cells) == 5:
                        input_t = cells[0] or input_t
                        cells = [cells[1], input_t, *cells[2:]]
                    rows.append(cells)
        parsed[label] = rows
        checks[label + ":reported_values_exact"] = rows == expected["rows"]
    components = {row[0]: row for row in parsed.get("tab:ablation-components", [])
                  if len(row) == 5}
    t8 = [row for row in parsed.get("tab:ablation-inputs", [])
          if len(row) == 5 and row[1] == "8"]
    checks["ablation_t8_consistent"] = (
        len(t8) == 2 and {row[0] for row in t8} == {"Ours", "w/o CCM"}
        and all(row[0] in components and row[3:5] ==
                [components[row[0]][1], components[row[0]][3]] for row in t8)
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-root", type=Path,
                        help="External cleanup archive; defaults to provenance/archive-map.json.")
    args = parser.parse_args()
    provenance = ROOT / "provenance"
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
    results_record = (json.loads(results_path.read_text(encoding="utf-8"))
                      if results_path.is_file() else None)
    frozen = [
        "fig/pointforward/Waymo.pdf", "fig/pointforward/nuScenes.pdf",
        "fig/pointforward/Shift.pdf", "cvpr.sty", "lineno.sty",
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
            checks["unchanged:" + name] = actual == original
            frozen_hashes[name] = {"sha256": actual, "original_sha256": original}
    details["frozen_hashes"] = frozen_hashes
    details["source_git_commit"] = manifest["source_git_commit"]

    overview_source = archive_root / archive_map["overview_original"]
    checks["overview_copy_exact"] = digest((ROOT / "fig/drivecompose-overview.png").read_bytes()) == digest(overview_source.read_bytes())
    details["raster_overview_role"] = "historical design draft; current entries use generated overview 20261021"
    overview = ROOT / "fig/drivecompose-overview-20261021.png"
    checks["generated_overview_exists"] = overview.is_file()
    for entry in ("main.tex", "main_zh.tex"):
        source = uncomment((ROOT / entry).read_text(encoding="utf-8"))
        checks[entry + ":generated_overview_active"] = (
            r"\includegraphics[width=\textwidth]{fig/drivecompose-overview-20261021.png}" in source
            and "drivecompose-overview.png" not in source
        )
    for language, name, heading in (("en", "sec/4_experiments.tex", "Experiments"),
                                     ("zh", "zh/4_experiments_zh.tex", "实验")):
        source = uncomment((ROOT / name).read_text(encoding="utf-8")).strip()
        if framework_record:
            required = ["sec:experiments", "sec:ablation-protocol", "sec:ablation-studies",
                        "sec:ablation-reuse", "tab:ablation-components", "tab:ablation-inputs"]
            empty_image_slots = results_record["empty_image_slots"] if results_record else 16
            if empty_image_slots:
                required.append("fig:ablation-reuse")
            checks[language + ":ablation_structure"] = (
                source.startswith("\\section{" + heading + "}")
                and all(source.count("\\label{" + label + "}") == 1 for label in required)
            )
            scoped_source = ablation_source(source)
            if results_record:
                checks.update({language + ":" + key: value for key, value in
                               reported_ablation_tables(scoped_source, results_record).items()})
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
        details["ablation_results_and_images_blank"] = not bool(results_record)
        details["ablation_results_filled"] = bool(results_record)
        details["ablation_images_blank"] = bool(
            results_record["empty_image_slots"] if results_record else 16
        )
        details["ablation_figure_removed"] = bool(
            results_record and results_record.get("ablation_figure_removed")
        )
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
