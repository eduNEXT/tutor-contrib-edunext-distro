import os
import subprocess

import click

from tutordistro.distro.domain.theme_repository import ThemeRepository
from tutordistro.distro.domain.clone_exception import CloneException
from tutordistro.distro.domain.theme_settings import ThemeSettings


class ThemeGitRepository(ThemeRepository):

    def clone(self, theme_settings: type(ThemeSettings)) -> None:
        if "https" == theme_settings.settings["protocol"]:
            repo = f"https://{theme_settings.settings['domain']}/\
            {theme_settings.settings['path']}/{theme_settings.settings['repo']}"
        elif "ssh" == theme_settings.settings["protocol"]:
            repo = f"git@{theme_settings.settings['domain']}:\
            {theme_settings.settings['path']}/{theme_settings.settings['repo']}"

        try:
            if os.path.exists(f"{theme_settings.get_full_directory}"):
                if not click.confirm(f"Do you want to overwrite \
                {theme_settings.get_full_directory}? "):
                    raise CloneException()

            subprocess.call(
                [
                    "git",
                    "clone",
                    "-b",
                    theme_settings.settings["version"],
                    repo,
                    f"{theme_settings.get_full_directory}",
                ]
            )
        except CloneException:
            pass
