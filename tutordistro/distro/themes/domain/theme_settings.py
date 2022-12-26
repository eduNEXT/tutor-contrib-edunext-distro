"""Theme settings."""
from typing import Dict

from tutor.types import Config


class ThemeSettings:
    """Theme settings."""
    def __init__(self, settings: Dict, tutor_root: str, tutor_config: Config):
        self.name = settings["name"]
        self.dir = f"env/build{tutor_config['DISTRO_THEMES_ROOT']}/{self.name}"
        self.tutor_path = str(tutor_root)
        self.settings = settings

    @property
    def get_full_directory(self) -> str:    # pylint: disable=missing-function-docstring
        return f"{self.tutor_path}/{self.dir}"
