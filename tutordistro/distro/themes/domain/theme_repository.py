from abc import ABC, abstractmethod

from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeRepository(ABC):
    @abstractmethod
    def clone(self, theme_settings: ThemeSettings) -> None:
        """
        Method to clone themes
        """
