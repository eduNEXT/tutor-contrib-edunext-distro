"""
Distro theme repository.
"""

from abc import ABC, abstractmethod

from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeRepository(ABC):
    """
    Abstract base class for theme repositories.

    This class defines the interface for theme repositories and provides
    an abstract method for cloning themes.
    """

    @abstractmethod
    def clone(self, theme_settings: ThemeSettings):
        """
        Clone a theme repository.

        This is an abstract method that should be implemented by subclasses.
        It defines the behavior for cloning a theme repository based on the
        provided theme settings.

        Args:
            theme_settings (ThemeSettings): The theme settings.
        """
