from abc import ABC, abstractmethod


class ThemeRepository(ABC):
    @abstractmethod
    def clone(self) -> None:
        """
        Method to clone themes
        """
