# Standard Library Imports
from typing import List

from solver.utils.text_cleaning import clean_answer_text

# Local Application Imports
from .base import BaseQuizType
from solver.utils.quiz_json import extract_answers_json


class MultipleChoiceQuiz(BaseQuizType):
    """
    Handles JetPunk quizzes with 'multiple choice' type questions.
    """

    def extract_answers(self) -> List[str]:
        answers = extract_answers_json(self.soup)
        unique_answers = []
        seen = set()

        for item in answers:
            choices = item.get("choices")
            correct_id = item.get("correct")
            if choices and correct_id:
                for choice in choices:
                    if choice.get("id") == correct_id:
                        answer_text = choice.get("text", "")
                        clean = clean_answer_text(answer_text)
                        if clean and clean not in seen:
                            unique_answers.append(answer_text)
                            seen.add(clean)

        return unique_answers
