"""
File of constant variables
"""
import re


def find_tutor_misspelled(command: str):
    """
    This function takes a command and looks if it has the word 'tutor' misspelled

    Args:
        command (str): Command to be reviewed

    Return:
        If its found the word 'tutor' misspelled is returned True
    """
    return re.match(r'[tT](?:[oru]{3}|[oru]{2}[rR]|[oru]u?)', command)
