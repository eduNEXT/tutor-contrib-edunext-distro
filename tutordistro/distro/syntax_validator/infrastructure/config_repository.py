"""
Infrastructure module to validate the configuration.
"""

from typing import List

import click

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_setting import ConfigSetting


class ConfigRepository:
    """
    Repository class for validating the configuration.

    This class provides methods to validate the configuration file using various validators.
    """

    def __init__(self, config_settings: List[ConfigSetting]):
        self.config_settings = config_settings

    def validate_syntax(self, config: ConfigFile) -> bool:
        """
        Validate the configuration file.

        Args:
            config: The configuration file to validate.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        try:
            for config_setting in self.config_settings:
                setting = config_setting(config=config)
                setting.validate()
            return True
        except Exception as error:  # pylint: disable=broad-exception-caught
            click.echo(error)
            return False
