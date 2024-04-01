"""
File of constant variables
"""
import re

COMMAND_CHAINING_OPERATORS = ["&&", "&", "||", "|", ";"]


def find_tutor_misspelled(command: str):
    """
    This function takes a command and looks if it has the word 'tutor' misspelled

    Args:
        command (str): Command to be reviewed

    Return:
        If its found the word 'tutor' misspelled is returned True
    """
    return re.match(r'[tT](?:[oru]{3}|[oru]{2}[rR]|[oru]u?)', command)


def create_regex_from_array(arr: list[str]):
    """
    This functions compiles a new regex turning taking care of
    escaping special characters

    Args:
        arr (list[str]): String that would be used to create a new regex

    Return:
        A new compiled regex pattern that can be used for comparisons
    """
    escaped_arr = [re.escape(item) for item in arr]
    regex_pattern = "|".join(escaped_arr)
    return re.compile(regex_pattern)
