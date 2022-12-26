"""Module to define the theme repository interface."""
from abc import ABC, abstractmethod

from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeRepository(ABC):  # pylint: disable=too-few-public-methods
    """Theme repository interface."""
    @abstractmethod
    def clone(self, theme_settings: ThemeSettings) -> None:
        """
        Method to clone themes
        """
