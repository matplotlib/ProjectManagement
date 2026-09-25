# Tools

## import_meeting_notes.py

### Configuration

Each meeting type should have a "live" note on HackMD as well as a corresponding directory in this Git repository. Currently, the script only imports the Weekly Meetings. New Contributors and GSOC could be added in the future.

Configuration is kept in `MEETING_DATA` at the top of the file:

```python
MEETING_DATA = [{
    "title": "Matplotlib Weekly Meeting",
    "note_id": "SyePADPcxx",  # https://hackmd.io/@matplotlib/SyePADPcxx
    "archive_dir": "meeting_notes",
    "prune_count": 4  # Keep last 4 meetings and save back to HackMD
}]
```

| Key | Description |
|-|-|
| `title` | Used as the title/first-heading for each archived .md file. |
| `note_id` | The HackMD note ID for the "live" note. |
| `archive_dir` | The path in the git repository to use as the meeting note archive. Relative to the repository root. |
| `prune_count` | If present, the number of meetings to keep in the "live" note. |

### HackMD API Key

The [HackMD API token](https://hackmd.io/@docs/how-to-issue-an-api-token) can be provided in one of the following ways:

- The `--hackmd-api-token` command-line argument.
- The `HACKMD_API_TOKEN` environment variable.
- A `.hackmd_api_token` file at the root level of the repository.


### HackMD Note Format

The HackMD note should have the following format:

```markdown
# First Heading

Some header information about the meeting.

<!--importer-start-->

# February 6, 2026

Notes for February 6 meeting.

# January 30th

Notes for January 30 meeting.

…etc.

<!--importer-end-->

An optional footer for the meeting.
```

- `<!--importer-start-->` is important, it tells the script where to start looking for meetings.
- `<!--importer-end-->` is optional. If missing, the script will assume that the end of the file is `<!--importer-end-->`.
- Each meeting must have a date as a `#` heading. The exact format of the date is flexible.
- No other `#` headings may be present between `<!--importer-start-->` and `<!--importer-end-->`.
- If using `prune_count`, only the content between `<!--importer-start-->` and `<!--importer-end-->` will be modified when the note is pruned.


### Overview of Import Process

1. The script iterates through all ".md" files in the `archive_dir` directory and extracts the notes for all existing meetings. 
2. The script downloads the latest meeting notes from HackMD using the [public API](https://hackmd.io/@docs/Getting-Started-with-the-HackMD-API). Any meetings in the "live" document will overwrite archived meetings.
3. The script creates a `%Y_%m_%b.md` file in the corresponding `%Y` directory for each month with meetings.


### Pruning

When `prune_count` is specified, the script will write an updated version of the "live" meeting notes back to HackMD with the latest `prune_count` meetings. To match historical usage, these will be arranged in reverse-chronological order (latest meeting on top).
