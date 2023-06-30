"""
Distro theme settings.
"""

from typing import Dict

from tutor.types import Config


class ThemeSettings:
    """
    Settings for a theme.

    This class represents the settings for a theme, including its name, directory,
    and other configuration options.

    Args:
        settings (Dict): The theme settings.
        tutor_root (str): The root directory of Tutor.
        tutor_config (Config): The Tutor configuration.

    Attributes:
        name (str): The name of the theme.
        dir (str): The directory of the theme.
        tutor_path (str): The path to Tutor.
        settings (Dict): The theme settings.
    """

    def __init__(self, settings: Dict, tutor_root: str, tutor_config: Config):
        self.name = settings["name"]
        self.dir = f"env/build{tutor_config['DISTRO_THEMES_ROOT']}/{self.name}"
        self.tutor_path = str(tutor_root)
        self.settings = settings

    @property
    def get_full_directory(self):
        """
        Get the full directory path of the theme.

        Returns:
            str: The full directory path of the theme.
        """
        return f"{self.tutor_path}/{self.dir}"
