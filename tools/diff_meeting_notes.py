#!/usr/bin/env python3

import argparse
import difflib
import subprocess
import sys
from pathlib import Path


def git(*args):
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def get_lines(commit: str, base_path: str):
    lines = []

    if commit == "working":
        for path in base_path.rglob("*"):
            if path.is_file() and not path.stem.startswith("."):
                with open(path, "r") as f:
                    lines.extend(f.readlines())
    else:
        output = git("ls-tree", "-r", "--name-only", commit, "--", str(base_path))
        for path in (output.splitlines() if output else [ ]):
            content = git("show", f"{commit}:{path}")
            lines.extend(content.splitlines(keepends=True))

    return sorted(lines)


def get_lenient_lines(in_lines: list[str]) -> list[str]:
    out_lines = []

    for line in sorted([s.strip() for s in in_lines]):
        if not out_lines or line != out_lines[-1]:
            out_lines.append(line)

    return out_lines
    

def main():
    parser = argparse.ArgumentParser(
        description="Diff contents of directory between two commits."
    )
    parser.add_argument("--dir", type=Path, default="meeting_notes", help="Directory to diff")
    parser.add_argument("--lenient", action="store_true", help="Unique sorted lines")
    parser.add_argument("commit1", help="Hash of first commit")
    parser.add_argument("commit2", help="Hash of second commit")
    args = parser.parse_args()

    try:
        lines1 = get_lines(args.commit1, args.dir)
        lines2 = get_lines(args.commit2, args.dir)
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr, end="")
        sys.exit(e.returncode)

    if args.lenient:
        lines1 = get_lenient_lines(lines1)
        lines2 = get_lenient_lines(lines2)
    else:
        lines1 = sorted(lines1)
        lines2 = sorted(lines2)

    diff = difflib.unified_diff(lines1, lines2, n = 0)
    
    for line in diff:
        if (
            line.startswith("+++") or
            line.startswith("---") or
            line.startswith("@@")
        ):
            continue
        if args.lenient:
            print(line)
        else:
            sys.stdout.write(line)

if __name__ == "__main__":
    main()
