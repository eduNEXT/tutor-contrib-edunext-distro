

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


class ValidateConfigUseCase:
    def __init__(self, config_repository: ConfigRepository):
        self.config_repository = config_repository

    def execute(self, file_path):
        config_file = ConfigFile(file_path)
        return self.config_repository.validate_config(config_file)
