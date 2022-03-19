import click
import subprocess
from tutor import config as tutor_config

@click.command(help="Enable distro theme volumes")
@click.pass_obj
def enable_theme_volumes(context) -> None:
    tutor_dir = str(context.root)
    config = tutor_config.load(context.root)

    for theme in config["DISTRO_THEME_VOLUMES"]:
        theme_dir = theme["src"]
        theme_repo = theme["repository"]
        theme_branch = theme["branch"]

        click.echo(f"creating {tutor_dir}/{theme_dir}...")
        subprocess.call(["mkdir", "-p", f"{tutor_dir}/{theme_dir}"])

        click.echo(f"clonning...")
        subprocess.call([
            "git",
            "clone",
            "-b",
            theme_branch,
            theme_repo,
            f"{tutor_dir}/{theme_dir}"
        ])
    click.echo("finishing...")
    click.echo("Theme volumes are enable now.")
