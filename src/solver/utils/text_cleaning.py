# Third Party Imports
from bs4 import BeautifulSoup
from unidecode import unidecode


def clean_answer_text(text: str) -> str:
    """
    Remove HTML tags and normalize unicode characters in answer text.
    """
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()

    # Normalize unicode characters
    text = unidecode(text)

    return text.strip()
