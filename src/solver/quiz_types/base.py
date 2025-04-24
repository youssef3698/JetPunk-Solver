# Standard Library Imports
from abc import ABC, abstractmethod

# Third Party Imports
from bs4 import BeautifulSoup


class BaseQuizType(ABC):
    """
    Abstract base class for all quiz types.
    """

    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    @abstractmethod
    def extract_answers(self):
        """
        Extract answers from the quiz page
        """
        pass
