"""
Tool to import meeting notes into per-month .md files
"""

# To use:
# 1) Open https://hackmd.io/@matplotlib/SyePADPcxx
# 2) Save the current meeting notes as a .md file (/path/to/import.md)
# 3) python tools/import_meeting_notes.py --into meeting_notes/2026 /path/to/import.md

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime, date


@dataclass
class Meeting:
    date: date
    lines: list[str]

    def trimmed_contents(self) -> str:
        """Removes leading/trailing lines which contain"""
        """only whitespace or horizontal rule characters."""
        lines = self.lines
        pattern = re.compile(r"^[\s\-_\*]*$")

        start = 0
        while start < len(lines) and pattern.match(lines[start]):
            start += 1

        end = len(lines)
        while end > start and pattern.match(lines[end - 1]):
            end -= 1

        return "\n".join(lines[start:end])


class InputFile:
    def __init__(self, path: Path, year: int):
        self.path = path
        self.year = year
        self.issues = []
        self.meetings_dict = {}

        with open(self.path, "r", encoding="utf-8") as f:
            contents = f.read()

        filename = self.path.stem
        contents = re.sub(r"<!--.*?-->", "", contents, flags=re.DOTALL)

        meeting = None
        HEADING_RE = re.compile(r"^#\s+(.+?)\s*$")
        FIRST_HEADING_RE = re.compile(r"^#\s+Matplotlib Weekly Meeting", re.IGNORECASE)

        for i, line in enumerate(contents.splitlines()):
            match = HEADING_RE.match(line)
            if match:
                date = parse_date(match.group(1), self.year)
                if date:
                    meeting = Meeting(date, [])
                    self.meetings_dict[date] = meeting
                elif not FIRST_HEADING_RE.match(line):
                    self.issues.append(
                        f"{filename}:{i + 1}: Found dateless heading: '{line}'"
                    )
            elif meeting is not None:
                meeting.lines.append(line)


def parse_date(date_str: str, default_year: int) -> date:
    """Parses a date string in various formats into a date"""
    text = date_str.strip()
    text = re.sub(r"(\d+)(st|nd|rd|th)\b", r"\1", text)
    text = re.sub(r"\bSept\b", "Sep", text)
    text = re.sub(r",\s+", " ", text)

    for value in (text, f"{text} {default_year}"):
        for fmt in [
            "%B %d %Y",  # August 5 2020
            "%b %d %Y",  # Aug 5 2020
            "%d %B %Y",  # 5 August 2020
            "%d %b %Y",  # 5 Aug 2020
        ]:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                pass

    return None


def get_year_from_path(path: Path) -> int | None:
    year = None
    for part in path.parts:
        if part.isdigit() and len(part) == 4:
            year = int(part)
    return year


def process_file(
    path: Path,
    year: int,
    meetings_dict: dict[date, Meeting],
    issues: list[str]
) -> None:
    input_file = InputFile(path, year)
    meetings_dict.update(input_file.meetings_dict)
    issues.extend(input_file.issues)


def get_meetings_by_month(
    meetings_dict: dict[date, Meeting],
    month: int
) -> None:
    meetings = meetings_dict.values()
    return sorted(
        (meeting for meeting in meetings if meeting.date.month == month),
        key=lambda meeting: meeting.date,
    )


def main():
    parser = argparse.ArgumentParser(description="Process meeting notes")
    parser.add_argument("--into", type=Path, required=True,
        help="Directory containing archived .md files")
    parser.add_argument("files", type=Path, nargs="*", help="Files to import")

    args = parser.parse_args()

    issues = []
    into_meetings_dict = {}
    import_meetings_dict = {}
    year = get_year_from_path(args.into)

    if not args.into.is_dir():
        raise ValueError(f"Path is not a directory: {args.into}")

    if year is None:
        raise ValueError(f"No year found in path: {args.into}")

    for path in args.into.glob("*.md"):
        process_file(path, year, into_meetings_dict, issues)

    for path in args.files:
        if path.is_dir():
            for md_path in path.glob("*.md"):
                process_file(md_path, year, import_meetings_dict, issues)
        elif path.exists():
            if path.suffix == ".md":
                process_file(path, year, import_meetings_dict, issues)
        else:
            raise ValueError(f"Could not read path: {path}")

    # Output meeting notes by month
    meetings_dict = {}
    meetings_dict.update(into_meetings_dict)
    meetings_dict.update(import_meetings_dict)

    if (
        len(get_meetings_by_month(meetings_dict, 1)) > 0 and
        len(get_meetings_by_month(meetings_dict, 12)) > 0
    ):
        issues.append("Import file(s) contain both January and December meetings.")

    for month in range(1, 13):
        meetings = get_meetings_by_month(meetings_dict, month)

        if len(meetings) == 0:
            continue

        month_date = date(year, month, 1)
        file_name = month_date.strftime("%Y_%m_%b.md").lower()

        output = [
            f"# Matplotlib Weekly Meeting: {month_date.strftime('%B %Y')}",
            "",
            f"###### tags: `{year} dev call`",
            ""
        ]

        for meeting in meetings:
            output.extend((
                "---",
                "",
                f"# {meeting.date.strftime('%B')} {meeting.date.day}, {year}",
                "",
                meeting.trimmed_contents(),
                ""
            ))

        meetings_noun = "meeting" if len(meetings) == 1 else "meetings"
        print(f"Wrote {len(meetings)} {meetings_noun} to '{args.into / file_name}'")
        with open(args.into / file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(output))

    if len(issues):
        print("")
        print("Issues:")
        print("=" * 80)
        for issue in issues:
            print(issue)


if __name__ == "__main__":
    main()
