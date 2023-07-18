"""
This module defines the ConfigSetting class, which represents a specific configuration.
"""
from abc import ABC, abstractmethod


class ConfigSetting(ABC):
    """
    This is an abstract class representing a specific configuration.
    """

    @abstractmethod
    def validate(self) -> None:
        """
        Validate the configuration.

        This method should be implemented in the derived class.
        """
