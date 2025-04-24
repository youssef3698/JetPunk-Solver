# Standard Library Imports
from pathlib import Path

# Third Party Imports
import configparser


CONFIG_PATH = Path(__file__).parent / "config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)


def get_timeout() -> float:
    """
    Get the timeout value from the config file.
    """
    try:
        return config.getfloat("network", "timeout")
    except Exception as e:
        print(f"Error reading timeout from config: {e}")
        return 10  # Default timeout value


def get_automation_delay() -> float:
    """
    Get the delay value from the config file.
    """
    try:
        return config.getfloat("automation", "delay")
    except Exception as e:
        print(f"Error reading delay from config: {e}")
        return 3  # Default delay value


def get_automation_sleep() -> float:
    """
    Get the sleep value from the config file.
    """
    try:
        return config.getfloat("automation", "sleep")
    except Exception as e:
        print(f"Error reading sleep from config: {e}")
        return 0.1  # Default sleep value
