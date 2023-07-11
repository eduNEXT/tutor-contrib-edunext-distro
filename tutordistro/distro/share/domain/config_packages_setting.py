"""
Domain module to structure packages validator.
"""
from schema import And, Optional, Or, Schema, SchemaError

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.share.domain.config_setting import ConfigSetting
from tutordistro.utils.packages import get_distro_packages


class ConfigPackagesSetting(ConfigSetting):
    """
    Represents a configuration setting for packages validation.

    This class is responsible for validating packages in the configuration.
    """

    def __init__(self, config: ConfigFile) -> None:
        self.config = config

    def validate(self) -> None:
        """
        Validate the packages in the configuration.

        Raises:
            ConfigFileValidationError: If a package validation fails.
        """
        package_schema = Schema(
            {
                "index": And(str, len),
                "name": And(str, len),
                "repo": And(str, len),
                "domain": And(str, len),
                "path": And(str, len),
                "protocol": Or("ssh", "https"),
                Optional("variables"): dict,
                "version": And(str, len),
                "private": And(bool)
            },
        )
        public_packages = get_distro_packages(self.config)
        for package in public_packages.values():
            try:
                package_schema.validate(package)
            except SchemaError as error:
                raise ConfigFileValidationError(package["name"], str(error)) from error
