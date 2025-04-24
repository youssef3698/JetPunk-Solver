# Standard Library Imports
import argparse

# Local Application Imports
from solver.utils.scraper import get_soup_from_url
from solver.utils.infer_quiz import infer_quiz_type
from solver.quiz_types.fill_in_the_blanks import FillInTheBlanksQuiz
from solver.quiz_types.multiple_choice import MultipleChoiceQuiz
from solver.quiz_types.all_words import AllWordsQuiz
from solver.utils.automation import wait_for_user, type_answers


def main():
    parser = argparse.ArgumentParser(description="JetPunk Quiz Solver")
    parser.add_argument("url", type=str, help="URL of the JetPunk quiz")
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatically type the answers into the quiz form",
    )
    args = parser.parse_args()

    # Get the HTML soup from the URL
    soup = get_soup_from_url(args.url)

    # Infer the quiz type
    quiz_type = infer_quiz_type(soup)

    # Initialize the appropriate quiz handler based on the inferred type
    if quiz_type == "multiple_choice":
        print("Detected multiple choice quiz.")
        quiz_handler = MultipleChoiceQuiz(soup)
    elif quiz_type == "fill_in_the_blank":
        print("Detected fill in the blank quiz.")
        quiz_handler = FillInTheBlanksQuiz(soup)
    elif quiz_type == "all_words":
        print("Detected all words quiz.")
        quiz_handler = AllWordsQuiz(soup)
    else:
        print("Unknown quiz type. Exiting.")
        return

    answers = quiz_handler.extract_answers()
    print(f"Extracted {len(answers)} answers.")

    if args.auto:
        wait_for_user()
        type_answers(answers)
    else:
        print("Answers:")
        for answer in answers:
            print(answer)


if __name__ == "__main__":
    main()
