# Standard Library Imports
import time
from typing import List

# Third Party Imports
import pyautogui

# Local Application Imports
from solver.config.config import get_automation_delay, get_automation_sleep
from solver.utils.text_cleaning import clean_answer_text


def clear_input_field() -> None:
    """
    Clears the currently focused input field.
    """
    pyautogui.hotkey("ctrl", "a")  # Select all text in the input field
    pyautogui.press("backspace")  # Delete the selected text


def type_answers(answers: List[str], submit: bool = False) -> None:
    """
    Types each answer into the currently focused input field using pyautogui.
    Optionally submits the answer after typing.
    """
    delay = get_automation_delay()
    sleep = get_automation_sleep()
    time.sleep(delay)  # Initial delay before typing
    for answer in answers:
        clean_answer = clean_answer_text(answer)
        pyautogui.typewrite(clean_answer)
        clear_input_field()
        if submit:
            pyautogui.press("enter")
        time.sleep(
            sleep
        )  # Sleep after each answer to avoid overwhelming the input field


def wait_for_user(message: str = "Press Enter to start typing...") -> None:
    """
    Waits for the user to press Enter before proceeding.
    """
    input(message)
