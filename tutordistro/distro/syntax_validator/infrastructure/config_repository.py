"""
Infrastructure module to validate the configuration.
"""

import click

from tutordistro.distro.syntax_validator.infrastructure.structure_validator import (
    validate_extra_files_requirements,
    validate_extra_pip_requirements,
    validate_extra_settings,
    validate_packages,
    validate_theme_settings,
    validate_themes,
)


class ConfigRepository:
    """
    Repository class for validating the configuration.

    This class provides methods to validate the configuration file using various validators.
    """

    def validate_config(self, config_file):
        """
        Validate the configuration file.

        Args:
            config_file: The configuration file to validate.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        try:
            config = config_file.file_path

            validate_packages(config)
            validate_extra_pip_requirements(config)
            validate_themes(config)
            validate_theme_settings(config)
            validate_extra_files_requirements(config)
            validate_extra_settings(config)

            return True
        except Exception as error:  # pylint: disable=broad-exception-caught
            click.echo(error)
            return False
