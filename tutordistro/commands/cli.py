"""
Distro commands group.
"""

import click

from tutordistro.commands.enable_private_packages import enable_private_packages
from tutordistro.commands.enable_themes import enable_themes
from tutordistro.commands.repository_validator import repository_validator

@click.group(help="Run distro commands")
def distro() -> None:
    """
    Main distro command group.

    This command group provides functionality to run distro commands.
    """


distro.add_command(enable_themes)
distro.add_command(enable_private_packages)
distro.add_command(repository_validator)
