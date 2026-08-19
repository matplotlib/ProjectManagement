#!/usr/bin/env python3

import argparse
import difflib
import subprocess
import sys


def git(*args):
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def get_sorted_lines(commit: str, base_path: str):
    lines = []

    output = git("ls-tree", "-r", "--name-only", commit, "--", base_path)
    for path in (output.splitlines() if output else [ ]):
        content = git("show", f"{commit}:{path}")
        lines.extend(content.splitlines(keepends=True))

    return sorted(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Diff contents of directory between two commits."
    )
    parser.add_argument("--dir", default="meeting_notes", help="Directory to diff")
    parser.add_argument("commit1", help="Hash of first commit")
    parser.add_argument("commit2", help="Hash of second commit")
    args = parser.parse_args()
    base_path = str(args.dir)

    try:
        lines1 = get_sorted_lines(args.commit1, base_path)
        lines2 = get_sorted_lines(args.commit2, base_path)
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr, end="")
        sys.exit(e.returncode)

    diff = difflib.unified_diff(
        lines1,
        lines2,
        n=0
    )
    
    for line in diff:
        if not line.startswith("@@"):
            sys.stdout.write(line)

if __name__ == "__main__":
    main()
