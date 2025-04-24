# Standard Library Imports
import re
import json
from typing import Any, List, Dict

# Third Party Imports
from bs4 import BeautifulSoup


def extract_answers_json(soup: BeautifulSoup) -> List[Dict[str, Any]]:
    """
    Extract answers from the JSON data embedded in the quiz page.

    Returns a list of answers.
    """

    script_tags = soup.find_all("script")
    json_data = None

    for script in script_tags:
        if "answers" in script.get_text():
            json_data = script.get_text()
            break
    if not json_data:
        return []

    match = re.search(r"var _page = ({.*?});", json_data, re.DOTALL)
    if not match:
        return []

    try:
        data = json.loads(match.group(1))
    except Exception:
        return []

    return data.get("data", {}).get("quiz", {}).get("answers", [])
