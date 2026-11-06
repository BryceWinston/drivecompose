"""Check permanent paper resources, bilingual math and repository cleanliness."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
FORMAL_PDFS = {'paper/build/en/main.pdf', 'paper/build/zh/main_zh.pdf',
               'paper/build/supp-en/main.pdf', 'paper/build/supp-zh/main_zh.pdf'}
FORMAL_BUILD_DIRS = {Path(name).parent.as_posix() for name in FORMAL_PDFS}
TEMP_DIRS = {'reviews', 'node_modules', '__pycache__', '.pytest_cache', '.build',
             '.tmp', 'tmp', '_archive', '.venv'}
TEMP_SUFFIXES = ('.aux', '.bbl', '.blg', '.brf', '.log', '.out', '.xdv', '.fls',
                 '.fdb_latexmk', '.synctex.gz', '.pyc', '.pyo', '.dtmp', '.bkp', '.bak', '.tmp')
RETIRED_FILES = {'docs/technical-review.md', 'docs/paper-literature-audit.md',
                 'docs/paper-narrative-review-20261021.md', 'docs/figures/teaser-cvpr-review.md',
                 'docs/paper-revision-changes.md', 'docs/paper-revision-workflow.md',
                 'paper/tools/reflow_teaser_pdf.py'}


def temporary_reason(name: str) -> str | None:
    path = Path(name)
    parts = path.parts
    if any(part in TEMP_DIRS for part in parts):
        return 'temporary directory'
    if name.startswith('paper/provenance/') or name == 'paper/provenance':
        return 'retired process records'
    if name.startswith('paper/build/') and name not in FORMAL_PDFS and name not in FORMAL_BUILD_DIRS:
        return 'non-final build output'
    if name in RETIRED_FILES:
        return 'retired review or workflow file'
    if name.endswith(TEMP_SUFFIXES):
        return 'temporary extension'
    if path.name in {'compile-result.json', 'compiler-output.txt', 'verification.json'}:
        return 'generated execution record'
    if re.search(r'(?:^|[-_])(preview|candidate|draft)(?:[-_.]|$)', path.name, re.I):
        return 'preview or candidate'
    return None


def working_violations() -> list[dict[str, str]]:
    violations = []
    for current, directories, files in os.walk(REPO):
        relative = Path(current).relative_to(REPO)
        for name in list(directories):
            if name == '.git':
                directories.remove(name)
                continue
            candidate = (relative / name).as_posix()
            reason = temporary_reason(candidate)
            if reason:
                violations.append({'path': candidate, 'reason': reason})
                directories.remove(name)
        for name in files:
            candidate = (relative / name).as_posix()
            reason = temporary_reason(candidate)
            if reason:
                violations.append({'path': candidate, 'reason': reason})
    return violations


def uncomment(text: str) -> str:
    return re.sub(r'(?<!\\)%[^\n]*', '', text)


def tex_document(entry: Path) -> tuple[str, list[str]]:
    pending, visited, content, missing = [entry], set(), [], []
    while pending:
        path = pending.pop()
        if path in visited:
            continue
        visited.add(path)
        source = uncomment(path.read_text(encoding='utf-8'))
        content.append(source)
        for kind, value in re.findall(r'\\(input|includegraphics|bibliography)(?:\[[^\]]*\])?\{([^}]+)\}', source):
            for name in value.split(','):
                target = entry.parent / name.strip()
                if kind == 'input' and not target.suffix:
                    target = target.with_suffix('.tex')
                elif kind == 'bibliography' and not target.suffix:
                    target = target.with_suffix('.bib')
                if not target.is_file():
                    missing.append(str(target.relative_to(REPO)))
                elif kind == 'input':
                    pending.append(target)
    return '\n'.join(content), missing


def math_blocks(path: Path) -> list[str]:
    source = uncomment(path.read_text(encoding='utf-8'))
    return [re.sub(r'\s+', '', re.sub(r'\\label\{[^}]+\}', '', body)).rstrip(',.')
            for _, body in re.findall(r'\\begin\{(equation|align)\}(.*?)\\end\{\1\}', source, re.S)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staged', action='store_true', help='Also inspect every indexed Git path, including paths ignored by .gitignore.')
    parser.add_argument('--output', type=Path, help='Optional report path; must be outside the repository.')
    args = parser.parse_args()
    output = (args.output or REPO.parent / '_archive/drivecompose/checks' /
              datetime.now().strftime('%Y%m%d-%H%M%S-%f') / 'manuscript-check.json').resolve()
    if output.is_relative_to(REPO):
        parser.error('Check reports must be written outside the repository.')

    checks, details = {}, {}
    violations = working_violations()
    checks['working_tree_has_no_temporary_files_including_ignored_files'] = not violations
    details['working_tree_violations'] = violations
    if args.staged:
        paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=REPO).decode('utf-8').split('\0')
        indexed = [{'path': path, 'reason': temporary_reason(path)} for path in paths if path and temporary_reason(path)]
        checks['git_index_has_no_temporary_files'] = not indexed
        details['index_violations'] = indexed

    for name in sorted(FORMAL_PDFS):
        checks[name + ':present'] = (REPO / name).is_file()
    for kind, entry, bibliography in [
        ('en', ROOT / 'main.tex', ROOT / 'main.bib'),
        ('zh', ROOT / 'main_zh.tex', ROOT / 'main.bib'),
        ('supp-en', ROOT / 'supplementary/main.tex', ROOT / 'supplementary/references.bib'),
        ('supp-zh', ROOT / 'supplementary/main_zh.tex', ROOT / 'supplementary/references.bib'),
    ]:
        text, missing = tex_document(entry)
        keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)', bibliography.read_text(encoding='utf-8'))
        cites = {key.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}', text) for key in group.split(',')}
        labels = re.findall(r'\\label\{([^}]+)\}', text)
        refs = {key.strip() for group in re.findall(r'\\(?:ref|eqref|cref|Cref)\{([^}]+)\}', text) for key in group.split(',')}
        checks[kind + ':resource_dependencies_resolve'] = not missing
        checks[kind + ':unique_bibliography_keys'] = len(keys) == len(set(keys))
        checks[kind + ':citations_resolve'] = cites <= set(keys)
        checks[kind + ':unique_labels'] = len(labels) == len(set(labels))
        checks[kind + ':cross_references_resolve'] = refs <= set(labels)
        details[kind] = {'missing_files': missing, 'missing_citations': sorted(cites - set(keys)), 'missing_labels': sorted(refs - set(labels)), 'bibliography_entries': len(keys)}

    english = math_blocks(ROOT / 'sec/3_method.tex')
    chinese = math_blocks(ROOT / 'zh/3_method_zh.tex')
    checks['bilingual_displayed_method_math_identical'] = bool(english) and english == chinese
    inline = []
    for name in ['sec/3_method.tex', 'zh/3_method_zh.tex']:
        inline.append(sorted(re.sub(r'\s+', '', item) for item in re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$', uncomment((ROOT / name).read_text(encoding='utf-8')), re.S)))
    checks['bilingual_inline_method_math_identical'] = inline[0] == inline[1]

    data = json.loads((ROOT / 'data/author-results.json').read_text(encoding='utf-8'))
    source = REPO / data['source']
    checks['structured_author_input_matches_original_text'] = source.is_file() and hashlib.sha256(source.read_bytes()).hexdigest() == data['source_sha256']
    for path in (ROOT / 'data').glob('*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    confirmation = json.loads((ROOT / 'data/author-ssim-confirmation.json').read_text(encoding='utf-8'))['after']
    for language, filename in [('en', 'sec/4_experiments.tex'), ('zh', 'zh/4_experiments_zh.tex')]:
        source_text = uncomment((ROOT / filename).read_text(encoding='utf-8'))
        tables = re.findall(r'\\begin\{(table\*?)\}(.*?)\\end\{\1\}', source_text, re.S)
        target = next((body for _, body in tables if r'\label{tab:regions_current}' in body), '')
        rows = {}
        for row in re.split(r'\\\\', target):
            cells = [re.sub(r'\\textbf\{([^{}]+)\}', r'\1', item).strip() for item in row.split('&')]
            if len(cells) > 2:
                for method in confirmation:
                    if re.search(r'(?<![\w])' + re.escape(method) + r'(?![\w])', cells[0]):
                        rows[method] = cells[2]
        checks[language + ':main_table_full_image_ssim_matches_author_confirmation'] = all(rows.get(method) == value for method, value in confirmation.items())

    failed = [name for name, passed in checks.items() if not passed]
    report = {'passed': not failed, 'checks': checks, 'details': details, 'failed': failed}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'passed': not failed, 'checks': len(checks), 'failed': failed, 'report': str(output)}, ensure_ascii=True))
    return int(bool(failed))


if __name__ == '__main__':
    sys.exit(main())
