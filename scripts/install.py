#!/usr/bin/env python3
"""Install only the rule block into Codex user instructions; no network calls."""
import argparse
import difflib
import os
from pathlib import Path
import re
import shutil
import tempfile

START = '<expert-epistemic-rules>'
END = '</expert-epistemic-rules>'


def merge(old, rules):
    if old.count(START) != old.count(END) or old.count(START) > 1:
        raise ValueError('Malformed or duplicate rule blocks; resolve manually before installing.')
    if START in old:
        if old.index(END) < old.index(START):
            raise ValueError('Rule block markers are out of order.')
        return re.sub(re.escape(START) + r'.*?' + re.escape(END),
                      lambda _: rules.strip(), old, count=1, flags=re.S)
    # Old releases suggested appending the full SKILL.md without markers.
    if '# Expert Epistemic Rules' in old or 'name: expert-epistemic-rules' in old:
        raise ValueError('Legacy unmarked skill found; migrate that section manually first.')
    return old + ('\n\n' if old and not old.endswith('\n') else '\n' if old else '') + rules.strip() + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=['codex'], required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    root = Path(os.environ.get('CODEX_HOME') or '~/.codex').expanduser().resolve()
    override = root / 'AGENTS.override.md'
    target = override if override.is_file() and override.read_text().strip() else root / 'AGENTS.md'
    # Follow an existing user-managed symlink rather than replacing it.
    target = target.resolve()
    rules = (Path(__file__).resolve().parent.parent / 'RULES.md').read_text(encoding='utf-8')
    if rules.count(START) != 1 or rules.count(END) != 1 or not rules.strip().startswith(START) or not rules.strip().endswith(END):
        raise ValueError('RULES.md must contain exactly one complete rule block.')
    old = target.read_bytes().decode('utf-8') if target.exists() else ''
    new = merge(old, rules)
    print(f'Target: {target}')
    if new == old:
        print('Already installed; no changes.')
        return
    if args.dry_run:
        print(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                         fromfile=str(target), tofile=str(target))), end='')
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        fd, backup = tempfile.mkstemp(prefix=target.name + '.backup-', dir=target.parent)
        os.close(fd)
        shutil.copy2(target, backup)
        print(f'Backup: {backup}')
    fd, temporary = tempfile.mkstemp(prefix=target.name + '.tmp-', dir=target.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(new.encode('utf-8'))
        if target.exists():
            shutil.copymode(target, temporary)
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    if target.read_bytes().decode('utf-8') != new:
        raise RuntimeError('Read-back verification failed.')
    print('Installed and read back. Start a fresh session to verify loading.')


if __name__ == '__main__':
    main()
