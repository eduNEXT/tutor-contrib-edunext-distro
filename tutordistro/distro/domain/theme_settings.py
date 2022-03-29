from tutor.types import Config
from typing import Dict


class ThemeSettings:
    def __init__(self, theme_settings: Dict, tutor_root: str, tutor_config: Config):
        self.dir = f"env/build/{tutor_config['DISTRO_THEMES_ROOT']}"
        self.tutor_path = str(tutor_root)
        self.branch = theme_settings["version"]
        self.protocol = theme_settings["protocol"]
        self.repo_name = theme_settings["repo"]

        if "https" == self.protocol:
            self.repo = f"https://{theme_settings['domain']}/{theme_settings['path']}/{theme_settings['repo']}"
        elif "ssh" == self.protocol:
            self.repo = f"git@{theme_settings['domain']}:{theme_settings['path']}/{theme_settings['repo']}"

    @property
    def get_full_directory(self) -> str:
        return f"{self.tutor_path}/{self.dir}"
