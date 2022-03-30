import os
import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.application.theme_enabler import ThemeEnabler
from tutordistro.distro.domain.theme_settings import ThemeSettings
from tutordistro.distro.domain.clone_exception import CloneException
from tutordistro.distro.infraestructure.distro_git_repository import DistroGitRepository


@click.command(name="enable-themes", help="Enable distro themes")
def enable_themes() -> None:
    directory = subprocess.check_output("tutor config printroot", shell=True).decode("utf-8").strip()
    config = tutor_config.load(directory)

    repository = DistroGitRepository()
    enabler = ThemeEnabler(repository=repository)

    for theme in config["DISTRO_THEMES"]:
        enabler(settings=theme, tutor_root=directory, tutor_config=config)
