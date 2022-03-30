import os
import subprocess

import click
from tutor import config as tutor_config
from tutordistro.distro.domain.theme_settings import ThemeSettings
from tutordistro.distro.domain.clone_exception import CloneException


@click.command(name="enable-themes", help="Enable distro themes")
def enable_themes() -> None:
    directory = subprocess.check_output("tutor config printroot", shell=True).decode("utf-8").strip()
    config = tutor_config.load(directory)

    for theme in config["DISTRO_THEMES"]:
        theme_settings = ThemeSettings(
            settings=theme, tutor_root=directory, tutor_config=config
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
        raise CloneException(
            f"""
            Finish not success. Error `subprocess api` {result}
            There are a trouble to enable themes.
            """
        )
