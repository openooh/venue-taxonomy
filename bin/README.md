# Venue Taxonomy Tools

## md_to_json.py

A Python tool built by Claude Sonnet to convert venue taxonomy specification from Markdown format to JSON format.

### Usage

```bash
./bin/md_to_json.py <input.md> <output.json>
```

Or with Python:

```bash
python3 ./bin/md_to_json.py <input.md> <output.json>
```

### Examples

Convert specification-1.1.md to JSON:

```bash
./bin/md_to_json.py specification-1.1.md specification-1.1.json
```

Convert specification-1.2.md to JSON:

```bash
./bin/md_to_json.py specification-1.2.md specification-1.2.json
```

### Features

- **Enumeration ID-based parsing**: Builds hierarchy based on the numeric structure of enumeration IDs (parent: 1-11, child: 101-1199, grandchild: 10101-119999)
- Automatically extracts version number from filename or version history table
- Parses all categories from markdown tables regardless of section headers
- Handles special character escaping (underscores, backslashes)
- Generates properly formatted JSON output matching the OpenOOH venue taxonomy schema
- Works with all specification versions (1.0, 1.1, 1.2, etc.)

### Input Format

The tool expects a Markdown file with tables containing venue categories. Each table row should have:
- Category name
- Description
- Enumeration ID (numeric identifier)
- String value (dot-separated path like `transit.airports.gates`)

The tool automatically identifies the hierarchy based on the enumeration ID structure:
- **Parent categories**: IDs 1-11
- **Child categories**: IDs 101-1199 (first 1-2 digits match parent)
- **Grandchild categories**: IDs 10101-119999 (first 2-4 digits match child)

No specific section headers are required - the tool scans all tables in the document.

### Output Format

The tool generates a JSON file with the following structure:

```json
{
  "openooh_venue_taxonomy": {
    "version": "1.1",
    "repository": "https://github.com/openooh/venue-taxonomy",
    "organization": "OpenOOH Working Group",
    "status": "accepted",
    "specification": {
      "categories": [
        {
          "name": "Transit",
          "description": "Transit",
          "enumeration_id": 1,
          "string_value": "transit",
          "children": [...]
        }
      ]
    }
  }
}
```

### Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Notes

- The tool handles markdown escaped underscores (`\_`) and converts them to regular underscores
- Trailing backslashes in table cells are automatically removed
- Version number is extracted from the filename (e.g., `specification-1.1.md` → version `1.1`)
- If version cannot be determined from filename, it falls back to parsing the version history table
