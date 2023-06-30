"""
Distro theme enabler config.
"""

from typing import Dict

from tutor.types import Config

from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeEnabler:
    """
    Theme enabler configuration.

    This class is responsible for enabling themes by invoking the clone method
    on a theme repository.

    Attributes:
        repository (ThemeRepository): The theme repository to use for cloning themes.
    """

    def __init__(self, repository: ThemeRepository):
        self.repository = repository

    def __call__(self, settings: Dict, tutor_root: str, tutor_config: Config):
        """
        Enable a theme based on the provided settings.

        This method enables a theme by creating theme settings and invoking
        the clone method on the theme repository.

        Args:
            settings (Dict): The theme settings.
            tutor_root (str): The root directory of the Tutor installation.
            tutor_config (Config): The Tutor configuration.
        """
        theme_settings = ThemeSettings(settings=settings, tutor_root=tutor_root,
                                       tutor_config=tutor_config)
        return self.repository.clone(theme_settings=theme_settings)
