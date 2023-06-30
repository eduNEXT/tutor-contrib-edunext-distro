"""
Distro config syntax validator command.
"""

import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.syntax_validator.application.validate_config_use_case import ValidateConfigUseCase
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


@click.command(name="syntax-validator", help="Syntax validator")
def syntax_validator() -> None:
    """
    Command to perform syntax validation on the configuration.

    This command loads the Tutor configuration, validates it using the
    ValidateConfigUseCase, and displays the validation result.
    """
    directory = subprocess.check_output("tutor config printroot", shell=True).decode("utf-8").strip()
    config = tutor_config.load(directory)

    config_repository = ConfigRepository()
    validate_config_use_case = ValidateConfigUseCase(config_repository)

    is_valid = validate_config_use_case.execute(config)

    if is_valid:
        click.echo("Success validation")
    else:
        click.echo("Failed validation. Check settings")
