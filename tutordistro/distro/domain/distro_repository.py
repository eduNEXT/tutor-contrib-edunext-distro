from abc import ABC, abstractmethod


class DistroRepository(ABC):
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
