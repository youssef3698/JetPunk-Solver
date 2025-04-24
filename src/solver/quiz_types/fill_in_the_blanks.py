# Standard Library Imports
from typing import List

from solver.utils.text_cleaning import clean_answer_text

# Local Application Imports
from .base import BaseQuizType
from solver.utils.quiz_json import extract_answers_json


class FillInTheBlanksQuiz(BaseQuizType):
    """
    Handles JetPunk quizzes with 'fill in the blank' type questions.
    """

    def extract_answers(self) -> List[str]:
        answers = extract_answers_json(self.soup)
        unique_answers = []
        seen = set()

        for item in answers:
            answer = item.get("display")
            if answer:
                clean = clean_answer_text(answer)
                if clean and clean not in seen:
                    unique_answers.append(answer)
                    seen.add(answer)

        return unique_answers
