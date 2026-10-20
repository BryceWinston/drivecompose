"""Build English/Chinese PDFs with an existing Tectonic executable."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def find_tectonic() -> Path | None:
    candidates = [os.environ.get("CODEX_TECTONIC_PATH"), shutil.which("tectonic")]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return Path(candidate).resolve()
    if os.name == "nt":
        powershell = (Path(os.environ.get("SystemRoot", "C:/Windows")) /
                      "System32/WindowsPowerShell/v1.0/powershell.exe")
        try:
            # WindowsApps cannot always be enumerated even when the installed
            # package's executable is readable. Ask Windows for its location.
            package = subprocess.run(
                [str(powershell), "-NoProfile", "-NonInteractive", "-Command",
                 "Get-AppxPackage -Name OpenAI.Codex | Select-Object -ExpandProperty InstallLocation"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            if package.returncode == 0:
                for directory in package.stdout.decode("utf-8", errors="replace").splitlines():
                    candidate = Path(directory.strip()) / "app/resources/tectonic/tectonic.exe"
                    if candidate.is_file():
                        return candidate.resolve()
        except (OSError, subprocess.TimeoutExpired):
            pass
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("en", "zh", "both"), default="both")
    args = parser.parse_args()
    executable = find_tectonic()
    if executable is None:
        parser.error("No Tectonic found in CODEX_TECTONIC_PATH, PATH, or the installed Codex app.")
    environment = {**os.environ, "TECTONIC_UNTRUSTED_MODE": "1"}
    if not environment.get("FONTCONFIG_FILE"):
        environment["FONTCONFIG_FILE"] = str(ROOT / "tools/fontconfig.conf")
    results = []
    for language, source in (("en", "main.tex"), ("zh", "main_zh.tex")):
        if args.language not in (language, "both"):
            continue
        out = ROOT / "build" / language
        out.mkdir(parents=True, exist_ok=True)
        pdf = out / Path(source).with_suffix(".pdf")
        previous_mtime = pdf.stat().st_mtime_ns if pdf.is_file() else None
        started_at = datetime.now(timezone.utc).isoformat()
        started = time.monotonic()
        command = [str(executable), "-X", "compile", "--outdir", str(out), "--outfmt", "pdf",
                   "--print", "--keep-logs", "--keep-intermediates", "--untrusted", source]
        run = subprocess.run(command, cwd=ROOT, env=environment,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = run.stdout.decode("utf-8", errors="replace")
        (out / "compiler-output.txt").write_text(output, encoding="utf-8")
        result = {"language": language, "command": command, "exit_code": run.returncode,
                  "started_at": started_at,
                  "finished_at": datetime.now(timezone.utc).isoformat(),
                  "elapsed_seconds": round(time.monotonic() - started, 3),
                  "fontconfig_file": environment["FONTCONFIG_FILE"],
                  "source_sha256": hashlib.sha256((ROOT / source).read_bytes()).hexdigest(),
                  "pdf": str(pdf), "pdf_exists": pdf.is_file(),
                  "pdf_written_this_run": pdf.is_file() and pdf.stat().st_mtime_ns != previous_mtime,
                  "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.is_file() else None}
        (out / "compile-result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        results.append(result)
        print(json.dumps(result, ensure_ascii=True), flush=True)
        if run.returncode:
            print(output[-6000:])
            return run.returncode
    return 0 if results and all(r["pdf_written_this_run"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
