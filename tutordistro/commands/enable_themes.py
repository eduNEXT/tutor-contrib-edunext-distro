"""
Distro enable theme command.
"""

import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.themes.application.theme_enabler import ThemeEnabler
from tutordistro.distro.themes.infraestructure.theme_git_repository import ThemeGitRepository


@click.command(name="enable-themes", help="Enable distro themes")
def enable_themes() -> None:
    """
    Enable distro themes.

    This function enables the themes specified in the `DISTRO_THEMES` configuration
    and applies them using the ThemeEnabler and ThemeGitRepository classes.
    """
    directory = subprocess.check_output("tutor config printroot", shell=True).\
        decode("utf-8").strip()
    config = tutor_config.load(directory)

    repository = ThemeGitRepository()
    enabler = ThemeEnabler(repository=repository)

    for theme in config["DISTRO_THEMES"]:
        enabler(settings=theme, tutor_root=directory, tutor_config=config)
