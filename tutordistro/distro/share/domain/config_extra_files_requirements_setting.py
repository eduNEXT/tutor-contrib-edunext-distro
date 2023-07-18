"""
Domain module to structure extra files requirements validator.
"""
from schema import And, Schema, SchemaError

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.share.domain.config_setting import ConfigSetting


class ConfigExtraFilesRequirementsSetting(ConfigSetting):
    """
    Represents a configuration setting for validating extra file requirements.

    This class is responsible for validating the extra file requirements in the configuration.
    """

    def __init__(self, config: ConfigFile) -> None:
        self.config = config

    def validate(self) -> None:
        """
        Validate the extra file requirements in the configuration.

        Raises:
            ConfigFileValidationError: If an extra file requirement validation fails.
        """
        extra_files_schema = Schema(
            {
                "files": And(list),
                "path": And(str, len),
            },
        )
        if "INSTALL_EXTRA_FILE_REQUIREMENTS" in self.config:
            try:
                extra_files_schema.validate(self.config["INSTALL_EXTRA_FILE_REQUIREMENTS"])
            except SchemaError as error:
                raise ConfigFileValidationError("INSTALL_EXTRA_FILE_REQUIREMENTS", str(error)) from error
