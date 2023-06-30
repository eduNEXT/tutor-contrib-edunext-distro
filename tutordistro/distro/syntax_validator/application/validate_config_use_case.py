"""
Aplication module to validate the configuration uses case.
"""

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


class ValidateConfigUseCase:
    """
    Use case class for validating a configuration file.

    This class encapsulates the logic for validating a configuration file
    using the provided ConfigRepository.
    """

    def __init__(self, config_repository: ConfigRepository):
        """
        Initialize the ValidateConfigUseCase.

        Args:
            config_repository (ConfigRepository): The repository to use for config validation.
        """
        self.config_repository = config_repository

    def execute(self, file_path):
        """
        Execute the configuration file validation.

        Args:
            file_path (str): The path to the configuration file.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        config_file = ConfigFile(file_path)
        return self.config_repository.validate_config(config_file)
