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
    parser.add_argument('--language', choices=('en', 'zh', 'both'), default='both')
    parser.add_argument('--material', choices=('main', 'supplementary', 'all'), default='main')
    parser.add_argument('--out-root', type=Path, help='Compilation directory outside the repository; defaults to a new external work directory.')
    parser.add_argument('--no-install', action='store_true', help='Compile candidates without replacing formal PDFs.')
    args = parser.parse_args()
    repo = ROOT.parent.resolve()
    out_root = (args.out_root or repo.parent / '_archive/drivecompose/builds' /
                datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S-%f')).resolve()
    if out_root.is_relative_to(repo):
        parser.error('Compilation, logs and result JSON must be outside the repository.')
    executable = find_tectonic()
    if executable is None:
        parser.error('No Tectonic found in CODEX_TECTONIC_PATH, PATH, or the installed Codex app.')
    environment = {**os.environ, 'TECTONIC_UNTRUSTED_MODE': '1'}
    environment.setdefault('FONTCONFIG_FILE', str(ROOT / 'tools/fontconfig.conf'))
    results = []
    for material in ('main', 'supplementary'):
        if args.material not in (material, 'all'):
            continue
        project = ROOT if material == 'main' else ROOT / 'supplementary'
        for language, source in (('en', 'main.tex'), ('zh', 'main_zh.tex')):
            if args.language not in (language, 'both'):
                continue
            kind = language if material == 'main' else 'supp-' + language
            out = out_root / kind
            out.mkdir(parents=True, exist_ok=True)
            pdf = out / Path(source).with_suffix('.pdf')
            previous_mtime = pdf.stat().st_mtime_ns if pdf.is_file() else None
            started_at = datetime.now(timezone.utc).isoformat()
            started = time.monotonic()
            command = [str(executable), '-X', 'compile', '--outdir', str(out), '--outfmt', 'pdf',
                       '--print', '--keep-logs', '--keep-intermediates', '--untrusted', source]
            print(json.dumps({'kind': kind, 'status': 'compiling', 'output_directory': str(out)}, ensure_ascii=True), flush=True)
            run = subprocess.run(command, cwd=project, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = run.stdout.decode('utf-8', errors='replace')
            (out / 'compiler-output.txt').write_text(output, encoding='utf-8')
            written = pdf.is_file() and pdf.stat().st_mtime_ns != previous_mtime
            result = {'language': language, 'material': material, 'command': command,
                      'exit_code': run.returncode, 'started_at': started_at,
                      'finished_at': datetime.now(timezone.utc).isoformat(),
                      'elapsed_seconds': round(time.monotonic() - started, 3),
                      'fontconfig_file': environment['FONTCONFIG_FILE'],
                      'source_sha256': hashlib.sha256((project / source).read_bytes()).hexdigest(),
                      'pdf': str(pdf), 'pdf_exists': pdf.is_file(), 'pdf_written_this_run': written,
                      'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.is_file() else None,
                      'installed_formal_pdf': None}
            if run.returncode == 0 and written and not args.no_install:
                formal = ROOT / 'build' / kind / Path(source).with_suffix('.pdf')
                formal.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copyfile(pdf, formal)
                except OSError as error:
                    result['installation_error'] = str(error)
                    result['exit_code'] = 1
                else:
                    if hashlib.sha256(formal.read_bytes()).hexdigest() != result['pdf_sha256']:
                        raise RuntimeError('Formal PDF copy hash mismatch')
                    result['installed_formal_pdf'] = str(formal)
            (out / 'compile-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            results.append(result)
            print(json.dumps(result, ensure_ascii=True), flush=True)
            if result['exit_code'] or not written:
                print(output[-6000:])
                return result['exit_code'] or 1
    return 0 if results else 1


if __name__ == '__main__':
    sys.exit(main())
