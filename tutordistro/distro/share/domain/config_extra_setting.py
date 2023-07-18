"""
Domain module to structure extra settings validator.
"""
from schema import And, Optional, Schema, SchemaError

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.share.domain.config_setting import ConfigSetting


class ConfigExtraSetting(ConfigSetting):
    """
    Represents a configuration setting for extra settings validation.

    This class is responsible for validating extra settings in the configuration.
    """

    def __init__(self, config: ConfigFile) -> None:
        self.config = config

    def validate(self) -> None:
        """
        Validate the extra settings in the configuration.

        Raises:
            ConfigFileValidationError: If an extra settings validation fails.
        """
        extra_settings_schema = Schema(
            {
                Optional("cms_env"): And(list),
                Optional("lms_env"): And(list),
                Optional("pre_init_lms_tasks"): And(list),
            },
        )
        extra_distro_settings_schemas = Schema(
            {
                Optional("DISTRO_EXTRA_MIDDLEWARES"): And(list),
                Optional("DISTRO_DISABLE_MFE"): And(bool),
            },
            ignore_extra_keys=True
        )
        if "OPENEDX_EXTRA_SETTINGS" in self.config:
            try:
                extra_settings_schema.validate(self.config["OPENEDX_EXTRA_SETTINGS"])
            except SchemaError as error:
                raise ConfigFileValidationError("OPENEDX_EXTRA_SETTINGS", str(error)) from error
        try:
            extra_distro_settings_schemas.validate(self.config)
        except SchemaError as error:
            raise ConfigFileValidationError("Settings", str(error)) from error
