import os
import shutil
import subprocess

import click
from tutor import config as tutor_config
from tutor.commands.context import Context

from .domain.theme_settings import ThemeSettings
from .domain.git_clone_exception import GitCloneException


@click.command(help="Enable distro themes")
@click.pass_obj
def enable_themes(context: Context) -> None:
    config = tutor_config.load(context.root)

    for theme in config["DISTRO_THEMES"]:
        theme_settings = ThemeSettings(
            theme_settings=theme, tutor_root=context.root, tutor_config=config
        )

        if os.path.isdir(f"{theme_settings.get_full_directory}"):
            click.echo("Cleaning cache...")
            subprocess.call(
                ["sudo", "rm", "-rf", f"{theme_settings.get_full_directory}"]
            )

        click.echo(f"creating {theme_settings.get_full_directory}...")
        subprocess.call(["mkdir", "-p", f"{theme_settings.get_full_directory}"])

        click.echo(f"clonning...")
        result = subprocess.call(
            [
                "git",
                "clone",
                "-b",
                theme_settings.branch,
                theme_settings.repo,
                f"{theme_settings.get_full_directory}/{theme_settings.repo}",
            ]
        )
    if result == 0:
        click.echo("finishing...")
        click.echo("Themes are enable now.")
    else:
        raise GitCloneException(
            f"""
            Finish not success. Error `subprocess api` {result}
            There are a trouble to enable themes.
            """
        )
