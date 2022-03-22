import click
import subprocess
from tutor import config as tutor_config
from tutor.commands.context import Context


@click.command(help="Enable distro themes")
@click.pass_obj
def enable_themes(context: Context) -> None:
    tutor_dir = str(context.root)
    config = tutor_config.load(context.root)

    for theme in config["DISTRO_THEMES"]:
        theme_dir = f"env/build{config['DISTRO_THEMES_ROOT']}"
        if "https" == theme["protocol"]:
            theme_repo = f"https://{theme['domain']}/{theme['path']}/{theme['repo']}"
        theme_branch = theme["version"]

        click.echo(f"creating {tutor_dir}/{theme_dir}...")
        subprocess.call(["mkdir", "-p", f"{tutor_dir}/{theme_dir}"])

        click.echo(f"clonning...")
        subprocess.call(
            ["git", "clone", "-b", theme_branch, theme_repo, f"{tutor_dir}/{theme_dir}"]
        )
    click.echo("finishing...")
    click.echo("Theme volumes are enable now.")
