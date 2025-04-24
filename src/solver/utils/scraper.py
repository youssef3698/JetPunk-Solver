# Standard Library Imports
from typing import Optional

# Third Party Imports
from bs4 import BeautifulSoup
import requests
import cloudscraper

# Local Application Imports
from solver.config.config import get_timeout


def fetch_quiz_html(url: str) -> Optional[str]:
    """
    Fetch the HTML content of a JetPunk quiz page.

    Returns the HTML as a string, or None if the request fails
    """

    timeout = get_timeout()

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
    }

    try:
        print(f"Fetching quiz HTML from {url}...")
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url, headers=headers, timeout=timeout)
        print("Request completed.")
        print(f"Response status code: {response.status_code}")
        print(f"Response content length: {len(response.content)} bytes")

        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching quiz HTML: {e}")
        return None


def get_soup_from_url(url: str) -> Optional[BeautifulSoup]:
    """
    Fetches the quiz page and returns a BeautifulSoup object.

    Returns None if the request fails.
    """

    html = fetch_quiz_html(url)

    if html is None:
        print("Failed to fetch HTML content.")
        return None

    return BeautifulSoup(html, "html.parser")
