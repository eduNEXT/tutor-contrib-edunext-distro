import os
import subprocess

import click

from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.packages.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeGitRepository(ThemeRepository):

    def clone(self, theme_settings: type(ThemeSettings)) -> None:
        if "https" == theme_settings.settings["protocol"]:
            repo = f"https://{theme_settings.settings['domain']}/{theme_settings.settings['path']}/{theme_settings.settings['repo']}"  #pylint: disable=line-too-long
        elif "ssh" == theme_settings.settings["protocol"]:
            repo = f"git@{theme_settings.settings['domain']}:{theme_settings.settings['path']}/{theme_settings.settings['repo']}.git"  #pylint: disable=line-too-long

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
