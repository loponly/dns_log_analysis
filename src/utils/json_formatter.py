from typing import Any, List
import json

def format_to_json(data: List[dict]) -> str:
    """
    Converts the analysis results into a structured JSON format.

    Args:
        data (List[dict]): The data to be converted to JSON.

    Returns:
        str: A JSON string representation of the data.
    """
    return json.dumps(data, indent=4)