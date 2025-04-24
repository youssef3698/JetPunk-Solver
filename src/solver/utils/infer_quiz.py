# Standard Library Imports
import re
import json
from typing import Literal

# Third Party Imports
from bs4 import BeautifulSoup


def infer_quiz_type(
    soup: BeautifulSoup,
) -> Literal[
    "multiple_choice",
    "fill_in_the_blank",
    "all_words",
    "unknown",
]:
    """
    Infer the JetPunk quiz type from the HTML soup.
    """

    script_tags = soup.find_all("script")
    json_data = None

    for script in script_tags:
        if "answers" in script.get_text():
            json_data = script.get_text()
            break
    if not json_data:
        return "unknown"

    match = re.search(r"var _page = ({.*?});", json_data, re.DOTALL)
    if not match:
        return "unknown"

    try:
        data = json.loads(match.group(1))
    except Exception:
        return "unknown"

    answers = data.get("data", {}).get("quiz", {}).get("answers", [])
    if not answers or not isinstance(answers, list):
        return "unknown"

    answer = answers[0]

    if "typeins" in answer:
        return "all_words"
    elif "display" in answer:
        return "fill_in_the_blank"
    elif "choices" in answer:
        return "multiple_choice"
    else:
        return "unknown"
