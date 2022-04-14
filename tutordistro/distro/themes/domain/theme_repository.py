from abc import ABC, abstractmethod


class ThemeRepository(ABC):
    @abstractmethod
    def clone(self, theme_settings) -> None:
        """
        Method to clone themes
        """
