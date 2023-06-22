"""
Distro theme funtions.
"""

import os
import shutil
import subprocess

import click

from tutordistro.distro.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeGitRepository(ThemeRepository):  # pylint: disable=too-few-public-methods
    """
    Git repository for themes.

    This class provides functionality to clone theme repositories.

    Args:
        ThemeRepository (class): Base theme repository class.
    """

    def clone(self, theme_settings: type(ThemeSettings)):
        """
        Clone the theme repository.

        This method clones the theme repository based on the provided theme settings.

        Args:
            theme_settings (ThemeSettings): Theme settings.
        """
        if "https" == theme_settings.settings["protocol"]:
            repo = (
                f"https://{theme_settings.settings['domain']}/"
                f"{theme_settings.settings['path']}/"
                f"{theme_settings.settings['repo']}"
            )
        elif "ssh" == theme_settings.settings["protocol"]:
            repo = (
                f"git@{theme_settings.settings['domain']}:"
                f"{theme_settings.settings['path']}/"
                f"{theme_settings.settings['repo']}.git"
            )

        try:
            if os.path.exists(f"{theme_settings.get_full_directory}"):
                if not click.confirm(f"Do you want to overwrite \
                {theme_settings.get_full_directory}? "):
                    raise CloneException()
                shutil.rmtree(f"{theme_settings.get_full_directory}")
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
