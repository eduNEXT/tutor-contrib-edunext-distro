from typing import Dict

from tutor.types import Config

from tutordistro.distro.domain.distro_repository import DistroRepository
from tutordistro.distro.domain.theme_settings import ThemeSettings


class ThemeEnabler:
    def __init__(self, repository: DistroRepository):
        self.repository = repository

    def __call__(self, settings: Dict, tutor_root: str, tutor_config: Config):
        theme_settings = ThemeSettings(settings=settings, tutor_root=tutor_root, tutor_config=tutor_config)
        self.repository.check_directory()
        return self.repository.clone(theme_settings=theme_settings)
