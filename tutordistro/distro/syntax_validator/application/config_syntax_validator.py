"""
Aplication module to validate the configuration uses case.
"""
from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


class ConfigSyntaxValidator:
    """
    Use case class for validating a configuration file.

    This class encapsulates the logic for validating a configuration file
    using the provided ConfigRepository.
    """

    def __init__(self, repository: ConfigRepository):
        """
        Initialize the ConfigValidor.

        Args:
            config_repository (ConfigRepository): The repository to use for config validation.
        """
        self.repository = repository

    def execute(self, file_path) -> bool:
        """
        Execute the configuration file validation.

        Args:
            file_path (str): The path to the configuration file.
        """
        config_file = ConfigFile(file_path)
        config = config_file.config_file()
        return self.repository.validate_syntax(config)
