# Standard Library Imports
from typing import List, Set
import re

# Local Application Imports
from .base import BaseQuizType
from solver.utils.quiz_json import extract_answers_json


class AllWordsQuiz(BaseQuizType):
    """
    Handles JetPunk quizzes with 'all words' type questions.
    """

    def get_first_answer(self, val: str) -> str:
        """
        Extracts the first answer from a string.
        """
        match = re.search(r"\(([^|)]+)", val)
        if match:
            return match.group(1)
        # Fallback: match after ^ if no parentheses are found
        match = re.search(r"\^?([A-Z]+)", val)
        if match:
            return match.group(1)
        return ""

    def extract_answers(self) -> List[str]:
        answers = extract_answers_json(self.soup)
        print(f"Extracted {len(answers)} answers from JSON.")
        print(f"Answers JSON: {answers}")
        unique_words: Set[str] = set()

        for item in answers:
            for typein in item.get("typeins", []):
                val = typein.get("val", "")
                if val:
                    first_answer = self.get_first_answer(val)
                    if first_answer:
                        unique_words.add(first_answer)
        return sorted(unique_words)
