"""
Module for handling configuration file validation errors.
"""


class ConfigFileValidationError(Exception):
    """
    Exception raised for syntax errors in configuration settings.

    Args:
        setting (str): The name of the setting with the syntax error.
        error_message (str): The error message describing the syntax error.

    Attributes:
        setting (str): The name of the setting with the syntax error.
        error_message (str): The error message describing the syntax error.
    """

    def __init__(self, setting, error_message):
        self.setting = setting
        self.error_message = error_message

    def __str__(self):
        return f"Syntax error in {self.setting}: {self.error_message}"
