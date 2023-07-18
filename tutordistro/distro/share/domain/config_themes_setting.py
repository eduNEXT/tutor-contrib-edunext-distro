"""
Domain module to structure themes validator.
"""

from schema import And, Optional, Or, Schema, SchemaError

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.share.domain.config_setting import ConfigSetting


class ConfigThemesSetting(ConfigSetting):
    """
    Validate the themes settings in the configuration.

    Raises:
        ConfigFileValidationError: If an extra file requirement validation fails.
    """

    def __init__(self, config: ConfigFile) -> None:
        self.config = config

    def validate(self) -> None:
        """
        Validate the themes in the configuration.

        Raises:
            ConfigFileValidationError: If a theme validation fails.
        """
        themes_schema = Schema(
            {
                "name": And(str, len),
                "repo": And(str, len),
                "domain": And(str, len),
                "path": And(str, len),
                "protocol": Or("ssh", "https"),
                "version": And(str, len),
            },
        )
        themes_settings_schema = Schema(
            {
                Optional("DISTRO_THEMES_NAME"): And(list, len),
                Optional("DISTRO_THEME_DIRS"): And(list, len),
                Optional("DISTRO_THEMES_ROOT"): And(str, len),
            },
            ignore_extra_keys=True
        )
        if "DISTRO_THEMES" in self.config:
            for theme in self.config["DISTRO_THEMES"]:
                try:
                    themes_schema.validate(theme)
                except SchemaError as error:
                    raise ConfigFileValidationError(theme["name"], str(error)) from error
        try:
            themes_settings_schema.validate(self.config)
        except SchemaError as error:
            raise ConfigFileValidationError("Theme settings", str(error)) from error
