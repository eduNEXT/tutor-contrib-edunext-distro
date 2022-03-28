from abc import ABC, abstractmethod


class DistroRepository(ABC):
    @abstractmethod
    def __init__(self, theme_settings, subprocess, click):
        """
        __init__ method
        Args:
            theme_settings (ThemeSettings): Domain attributes to manage theme settings
            subprocess (subprocess)
            click (click)
        """
        pass

    @abstractmethod
    def clone(self, theme_settings) -> None:
        """
        Method to clone themes
        """

    @abstractmethod
    def check_directory(self, os) -> None:
        """
        Method to check if theme directory already exists
        """

    @abstractmethod
    def create_directory(self) -> None:
        """
        Method to clean old theme directory
        """
