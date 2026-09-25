"""
Tool to automatically import meeting notes using the HackMD API.
"""

import argparse
import json as _json
import os
import re
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


MEETING_DATA = [{
    "title": "Matplotlib Weekly Meeting",
    "note_id": "SyePADPcxx",  # https://hackmd.io/@matplotlib/SyePADPcxx
    "archive_dir": "meeting_notes",
    "prune_count": 4  # Keep last 4 meetings and save back to HackMD
}]

HEADING_RE = re.compile(r"^#\s+(.+?)\s*$")

HEADING_WITH_DATE_RE = re.compile(r"""
    ^\# # 1st-level heading
    (?:.*?) # Optional text before date
    (
        \d{1,2}/\d{1,2}/\d{4} | # 08/25/1982
        \d{1,2}/\d{1,2}/\d{2} | # 08/25/82
        (?: # Group that handles "Aug 25, 1982" / "25th Aug" / etc.
            (?:\d+\s*(?:nd|rd|st|th)?\s+)? # Match a day before the month
            (?: # Month name
                January|February|March|April|May|June|
                July|August|September|October|November|December|
                Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec
            )
            (?:\s+\d+\s*(?:nd|rd|st|th)?)? # Match a day after the month
            (?:[\s,]*)? # Optional whitespace or comma
            (?:[\d]{4})? # Optional year
        )
    )
    (?:\s+.*?)?$ # Optional text after date
""", re.VERBOSE | re.IGNORECASE)

IMPORTER_START_RE = re.compile(r"^\s*<!--\s*importer[- ]start\s*-->\s*$")
IMPORTER_END_RE = re.compile(r"^\s*<!--\s*importer[- ]end\s*-->\s*$")

WHITESPACE_OR_HORIZONTAL_RULE_RE = re.compile(r"^[\s\-_\*]*$")
USERNAME_LINK_RE = re.compile(r"\[(\@[\w\-_]+)\]\(\@[\w\-_]+\)")


@dataclass
class Meeting:
    date: date
    lines: list[str]


@dataclass
class Document:
    header: str
    footer: str | None
    meetings: list[Meeting]


def get_repository_path():
    script_path = Path(__file__).resolve()

    for parent in [script_path.parent, *script_path.parents]:
        if (parent / ".git").exists():
            return parent

    raise RuntimeError("Could not find git repository root")


def write_contents(path: Path, contents: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents, encoding="utf-8")


def call_hackmd_api(
    api_token: str,
    url: str,
    json: dict | None = None,
    method: str | None = None
) -> dict:
    request = urllib.request.Request(
        url,
        data=_json.dumps(json).encode("utf-8") if json is not None else None,
        headers={
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        },
        method=method
    )

    with urllib.request.urlopen(request) as response:
        response_bytes = response.read()
        encoding = response.headers.get_content_charset("utf-8")
        response_text = response_bytes.decode(encoding)
        result = _json.loads(response_text) if response_text else {}

    return result


def get_team_note_url(note_id: str) -> str:
    return f"https://api.hackmd.io/v1/teams/matplotlib/notes/{note_id}"


def save_to_hackmd(
    api_token: str,
    note_id: str,
    contents: str,
    debug_path: Path | None = None
) -> None:
    if (debug_path):
        write_contents(debug_path / "output" / f"{note_id}.md", contents)
    else:
        call_hackmd_api(
            api_token,
            url=get_team_note_url(note_id),
            json={"content": contents},
            method="PATCH"
        )


def load_from_hackmd(
    api_token: str,
    note_id: str,
    debug_path: Path | None = None
) -> str:
    if debug_path:
        local_md_path = debug_path / "input" / f"{note_id}.md"
        with open(local_md_path, "r", encoding="utf-8") as f:
            contents = f.read()
        return contents
    else:
        url = get_team_note_url(note_id)
        response_dict = call_hackmd_api(api_token, url)
        return response_dict["content"]


def get_date_from_heading(heading: str) -> date | None:
    """Attempts to extract a date from a Level 1 Heading (#)."""
    match = HEADING_WITH_DATE_RE.match(heading)

    if match:
        text = match[1].strip()
        text = re.sub(r"(\d+)(nd|rd|st|th)\b", r"\1", text)
        text = re.sub(r"\bSept\b", "Sep", text)
        text = re.sub(r",\s+", " ", text)

        for fmt in [
            "%m/%d/%y",  # 8/25/82
            "%m/%d/%Y",  # 8/25/1982
            "%B %d %Y",  # August 25 1982
            "%b %d %Y",  # Aug 25 1982
            "%d %B %Y",  # 25 August 1982
            "%d %b %Y",  # 25 Aug 1982
        ]:
            try:
                return date.strptime(text, fmt)
            except ValueError:
                pass

    return None


def get_meetings_from_lines(
    lines: list[str],
    filename: str
) -> list[Meeting]:
    meetings = []
    meeting = None

    for line in lines:
        if match := HEADING_RE.match(line):
            date = get_date_from_heading(line)

            if date is None:
                raise ValueError(
                    f"{filename}: Could not get date from heading '{line}'"
                )

            meeting = Meeting(date, [])
            meetings.append(meeting)
        elif meeting is not None:
            meeting.lines.append(line)

    return meetings


def get_meetings_from_archive_path(path: Path) -> list[Meeting]:
    """Reads an on-disk Markdown file and extracts a list of Meeting objects."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if len(lines) == 0 or HEADING_RE.match(lines[0]) is None:
        raise ValueError(f"{path.name}: Could not find first heading")

    return get_meetings_from_lines(lines[1:], path.name)


def get_document_from_hackmd_note(note_id: str, contents: str) -> Document:
    """Parses a Markdown content string and creates a *Document*."""
    lines = contents.splitlines()

    # Find <!--importer-start--> comment
    try:
        start = next(
            i for i, line in enumerate(lines)
            if IMPORTER_START_RE.match(line)
        )
    except StopIteration:
        raise ValueError(f"{note_id}: Missing <!--importer-start-->")

    # Find <!--importer-end--> comment
    try:
        end = next(
            i for i, line in enumerate(lines)
            if IMPORTER_END_RE.match(line)
        )
    except StopIteration:
        end = len(lines)

    return Document(
        "\n".join(lines[:start + 1]),
        "\n".join(lines[end:]),
        get_meetings_from_lines(lines[start+1:end], note_id)
    )


def get_meeting_string(meeting: Meeting) -> str:
    """Returns a Markdown string containing the meeting's content."""
    """Leading/trailing whitespace lines and horizontal rule lines are removed."""
    """Hackmd username links are converted to `@github_username`."""
    lines = meeting.lines

    start = 0
    while start < len(lines) and WHITESPACE_OR_HORIZONTAL_RULE_RE.match(lines[start]):
        start += 1

    end = len(lines)
    while end > start and WHITESPACE_OR_HORIZONTAL_RULE_RE.match(lines[end - 1]):
        end -= 1

    result = "\n".join(lines[start:end])

    # Convert '[@efiring](@QWhXj01mSwmTjk5kN1H_qQ)' to '@efiring'
    result = USERNAME_LINK_RE.sub(r"\1", result)

    return result


def get_meetings_string(meetings: list[Meeting]) -> str:
    """Generates a content string for the list of meetings."""
    result = []

    for meeting in meetings:
        date = meeting.date

        result.extend((
            "---",
            "",
            f"# {date.strftime('%B')} {date.day}, {date.year}",
            "",
            get_meeting_string(meeting),
            ""
        ))

    return "\n".join(result)


def get_pruned_contents(document: Document, prune_count: int) -> str:
    """Generates a content string containing *document*'s header, footer, and"""
    """*prune_count* meetings (sorted in reverse-chronological order)."""
    output = []

    if document.header:
        output.append(document.header)

    latest_meetings = sorted(
        document.meetings,
        key=lambda m: m.date, reverse=True
    )[:prune_count]

    output.extend(("", get_meetings_string(latest_meetings)))

    if document.footer:
        output.append(document.footer)

    return "\n".join(output)


def import_meetings(
    archive_path: Path,
    title: str,
    in_meetings: list[Meeting]
) -> None:
    year_month_re = re.compile(r"\d{4}_\d{2}")
    meetings_by_month = defaultdict(list)

    def add_meeting(meeting: Meeting) -> None:
        meetings_by_month[(meeting.date.year, meeting.date.month)].append(meeting)

    # Grab all existing meetings
    for path in archive_path.rglob("*.md"):
        if year_month_re.search(path.stem):
            for meeting in get_meetings_from_archive_path(path):
                add_meeting(meeting)

    # Add new meetings
    for meeting in in_meetings:
        add_meeting(meeting)

    if len(meetings_by_month) == 0:
        return

    min_year = min(year for year, month in meetings_by_month)
    max_year = max(year for year, month in meetings_by_month)

    for year in range(min_year, max_year + 1):
        for month in range(1, 13):
            meetings = sorted(
                meetings_by_month[(year, month)],
                key=lambda meeting: meeting.date
            )

            if len(meetings) == 0:
                continue

            month_date = date(year, month, 1)
            file_name = month_date.strftime("%Y_%m_%b.md").lower()

            write_contents(archive_path / f"{year}" / file_name, "\n".join([
                f"# {title}: {month_date.strftime('%B %Y')}",
                "",
                get_meetings_string(meetings)
            ]))


def main():
    parser = argparse.ArgumentParser(description="Import meeting notes from HackMD")
    parser.add_argument("--debug-path", type=Path,
        help="Use local directory instead of calling the HackMD API (for debug)")
    parser.add_argument("--hackmd-api-token",
        help="Access token for HackMD API")

    args = parser.parse_args()
    debug_path = args.debug_path
    repo_path = get_repository_path()

    api_token = None
    if debug_path is None:
        api_token = args.hackmd_api_token
        if api_token is None:
            api_token = os.getenv("HACKMD_API_TOKEN")
        if api_token is None:
            token_path = repo_path / ".hackmd_api_token"
            if token_path.exists():
                api_token = token_path.read_text().strip()

    if api_token is None:
        raise ValueError("A HackMD API token was not found")

    for meeting_data_dict in MEETING_DATA:
        note_id = meeting_data_dict["note_id"]
        title = meeting_data_dict["title"]
        prune_count = meeting_data_dict.get("prune_count")
        archive_path = repo_path / meeting_data_dict["archive_dir"]

        hackmd_note_content = load_from_hackmd(api_token, note_id, debug_path)
        document = get_document_from_hackmd_note(note_id, hackmd_note_content)
        import_meetings(archive_path, title, document.meetings)

        if prune_count is not None:
            updated_content = get_pruned_contents(document, prune_count)
            if updated_content != hackmd_note_content:
                save_to_hackmd(api_token, note_id, updated_content, debug_path)


if __name__ == "__main__":
    main()
