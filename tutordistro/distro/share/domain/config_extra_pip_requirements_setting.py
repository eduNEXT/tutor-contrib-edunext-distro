"""
Domain module to structure extra pip requirements validator.
"""
from schema import Schema, SchemaError

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.share.domain.config_setting import ConfigSetting


class ConfigExtraPipRequirementsSetting(ConfigSetting):
    """
    Represents a configuration setting for validating extra pip requirements.

    This class is responsible for validating the extra pip requirements in the configuration.
    """

    def __init__(self, config: ConfigFile) -> None:
        self.config = config

    def validate(self) -> None:
        """
        Validate the extra pip requirements in the configuration.

        Raises:
            ConfigFileValidationError: If an extra pip requirement validation fails.
        """
        pip_requirement_schema = Schema(str, len)
        if "OPENEDX_EXTRA_PIP_REQUIREMENTS" in self.config:
            ep_requirements = self.config["OPENEDX_EXTRA_PIP_REQUIREMENTS"]
            for requirement in ep_requirements:
                try:
                    pip_requirement_schema.validate(requirement)
                except SchemaError as error:
                    raise ConfigFileValidationError(requirement, str(error)) from error
