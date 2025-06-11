from typing import Any, List
import json
import re

def format_to_json(data: dict) -> str:
    """
    Converts the analysis results into a structured JSON format.

    Args:
        data (dict): The data to be converted to JSON.

    Returns:
        str: A JSON string representation of the data.
    """
    # First, generate the JSON with standard formatting
    json_str = json.dumps(data, indent=4, ensure_ascii=False, separators=(",", ": "))
    
    # Post-process to make arrays compact while keeping object indentation
    # This regex finds arrays that span multiple lines and makes them compact
    def compact_array(match):
        array_content = match.group(1)
        # Remove all whitespace and newlines, then format compactly
        items = [item.strip() for item in array_content.split(',') if item.strip()]
        if not items:
            return '[]'
        return '[' + ', '.join(items) + ']'
    
    # Pattern to match arrays that span multiple lines
    pattern = r'\[\s*\n\s*([^[\]]*?)\s*\n\s*\]'
    json_str = re.sub(pattern, compact_array, json_str, flags=re.DOTALL)
    
    return json_str