"""
Module for handling configuration files.
"""
from tutor import config as tutor_config


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

    def config_file(self):
        """
        Load and return the configuration file.

        Returns:
            dict: The loaded configuration file.

        Note:
            This method uses the 'tutor_config.load' function to load the configuration file.
        """
        return tutor_config.load(self.file_path)
