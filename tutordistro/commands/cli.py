import click

from tutordistro.commands.enable_themes import enable_themes
from tutordistro.commands.enable_private_packages import enable_private_packages

@click.group(help="Run distro commands")
def distro() -> None:
    pass

distro.add_command(enable_themes)
distro.add_command(enable_private_packages)
