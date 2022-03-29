from typing import Dict

from tutordistro.distro.domain.distro_repository import DistroRepository
from tutordistro.distro.domain.theme_settings import ThemeSettings


class ThemesEnabler:
    def __init__(self, repository: DistroRepository):
        self.repository = repository

    def __call__(self, settings: Dict):
        theme_settings = ThemeSettings(settings)
        self.repository.check_directory()
        return self.repository.clone(theme_settings)
