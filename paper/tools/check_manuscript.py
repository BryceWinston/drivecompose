"""Check frozen experiments, manuscript dependencies, citations and bilingual math."""
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
    frozen = manifest["frozen_experiments"] + [
        "fig/pointforward/Waymo.pdf", "fig/pointforward/nuScenes.pdf",
        "fig/pointforward/Shift.pdf", "cvpr.sty", "lineno.sty",
        "ieeenat_fullname.bst", "preamble.tex",
    ]
    with zipfile.ZipFile(archive_path) as archive:
        frozen_hashes = {}
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
    details["frozen_experiments_intentionally_not_synchronized"] = True
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
