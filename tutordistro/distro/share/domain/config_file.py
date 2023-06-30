"""
Module for handling configuration files.
"""


class ConfigFile:
    """
    Represents a configuration file.

    Args:
        file_path (str): The path to the configuration file.

    Attributes:
        file_path (str): The path to the configuration file.
    """

    def __init__(self, file_path):
        self.file_path = file_path
