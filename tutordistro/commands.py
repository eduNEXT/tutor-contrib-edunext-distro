import click
import subprocess
from tutor import config as tutor_config

@click.command(help="Enable distro theme volumes")
@click.pass_obj
def enable_theme_volumes(context) -> None:
    tutor_dir = str(context.root)
    theme_dir = "env/build/openedx/distro-themes/ednx-saas-themes"
    click.echo(f"creating {tutor_dir}/{theme_dir}...")
    subprocess.call(["mkdir", "-p", f"{tutor_dir}/{theme_dir}"])

    click.echo(f"clonning..")
    subprocess.call([
        "git",
        "clone",
        "-b",
        "edunext/mango.master",
        f"git@github.com:eduNEXT/ednx-saas-themes.git",
        f"{tutor_dir}/{theme_dir}"
    ])
    click.echo(f"finishing...")
    click.echo("Theme volumes are enable now.")
