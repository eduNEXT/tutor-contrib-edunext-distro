"""Theme enabler module."""
from typing import Dict

from tutor.types import Config

from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeEnabler:  # pylint: disable=too-few-public-methods
    """Theme enabler."""
    def __init__(self, repository: ThemeRepository):
        self.repository = repository

    def __call__(self, settings: Dict, tutor_root: str, tutor_config: Config):
        theme_settings = ThemeSettings(settings=settings, tutor_root=tutor_root,
                                       tutor_config=tutor_config)
        return self.repository.clone(theme_settings=theme_settings)
