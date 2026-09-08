#!/usr/bin/env python3
"""

Thanks Claude Sonnet
---

Convert venue taxonomy specification from Markdown to JSON format.

Usage:
    python md_to_json.py <input.md> <output.json>
    or
    ./md_to_json.py specification-1.1.md specification-1.1.json
"""

import sys
import re
import json
from typing import Dict, List


def extract_version(content: str, filename: str = "") -> str:
    """Extract version number from the markdown content or filename."""
    # First try to extract from filename (e.g., specification-1.1.md)
    if filename:
        filename_pattern = r'specification-(\d+\.\d+)\.md'
        match = re.search(filename_pattern, filename)
        if match:
            return match.group(1)
    
    # Look for version in the version history table
    cleaned_content = re.sub(r'\|\s*\n\s*', '| ', content)
    version_pattern = r'\|\s*(\d+\.\d+\.\d+)\s*\|'
    matches = re.findall(version_pattern, cleaned_content)
    if matches:
        versions = []
        for v in matches:
            parts = v.split('.')
            if len(parts) == 3:
                versions.append((int(parts[0]), int(parts[1]), int(parts[2]), v))
        
        if versions:
            versions.sort(reverse=True)
            version = versions[0][3]
            parts = version.split('.')
            return f"{parts[0]}.{parts[1]}"
    
    return "1.0"


def extract_all_categories(content: str) -> Dict[int, Dict]:
    """Extract all categories from markdown by parsing all tables.
    
    Returns a dictionary mapping enumeration_id to category info.
    """
    lines = content.split('\n')
    categories = {}
    
    for i, line in enumerate(lines):
        if not line.strip().startswith('|'):
            continue
        
        if not re.search(r'\|\s*\d+\s*\|', line):
            continue
        
        cells = [c.strip() for c in line.split('|') if c.strip()]
        cells = [c.replace('\\_', '_').rstrip('\\').strip() for c in cells]
        
        enum_id = None
        name = None
        description = None
        string_value = None
        
        if len(cells) >= 3:
            for idx, cell in enumerate(cells):
                if re.match(r'^\d{1,6}$', cell):
                    enum_id = int(cell)
                    name = cells[0]
                    if idx + 1 < len(cells):
                        string_value = cells[-1]
                    if len(cells) >= 4:
                        description = cells[1]
                    else:
                        description = name
                    break
        
        if enum_id and name and string_value:
            if '.' in string_value or '_' in string_value or re.match(r'^[a-z_]+$', string_value):
                categories[enum_id] = {
                    'name': name,
                    'description': description,
                    'enumeration_id': enum_id,
                    'string_value': string_value
                }
    
    return categories


def build_hierarchy(categories: Dict[int, Dict]) -> List[Dict]:
    """Build hierarchical structure based on enumeration ID patterns."""
    parents = {id: cat for id, cat in categories.items() if 1 <= id <= 11}
    
    result = []
    for parent_id in sorted(parents.keys()):
        parent = parents[parent_id].copy()
        parent['children'] = []
        
        child_start = parent_id * 100
        child_end = child_start + 99
        
        for child_id in sorted(categories.keys()):
            if child_start <= child_id <= child_end:
                child = categories[child_id].copy()
                child['children'] = []
                
                grandchild_start = child_id * 100
                grandchild_end = grandchild_start + 99
                
                for grandchild_id in sorted(categories.keys()):
                    if grandchild_start <= grandchild_id <= grandchild_end:
                        grandchild = categories[grandchild_id].copy()
                        child['children'].append(grandchild)
                
                if not child['children']:
                    del child['children']
                
                parent['children'].append(child)
        
        if not parent['children']:
            del parent['children']
        
        result.append(parent)
    
    return result


def build_taxonomy(content: str, filename: str = "") -> Dict:
    """Build the complete taxonomy structure from markdown content."""
    version = extract_version(content, filename)
    categories = extract_all_categories(content)
    hierarchy = build_hierarchy(categories)
    
    taxonomy = {
        'openooh_venue_taxonomy': {
            'version': version,
            'repository': 'https://github.com/openooh/venue-taxonomy',
            'organization': 'OpenOOH Working Group',
            'status': 'accepted',
            'specification': {
                'categories': hierarchy
            }
        }
    }
    
    return taxonomy


def main():
    if len(sys.argv) != 3:
        print("Usage: python md_to_json.py <input.md> <output.json>")
        print("Example: python md_to_json.py specification-1.1.md specification-1.1.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        taxonomy = build_taxonomy(content, input_file)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(taxonomy, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully converted {input_file} to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
