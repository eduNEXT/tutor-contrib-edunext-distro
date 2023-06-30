"""
Infrastructure module to structure validator of the configuration file.
"""

from schema import And, Optional, Or, Schema, SchemaError

from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.utils.packages import get_distro_packages


def validate_packages(config):
    """
    Validate the packages in the configuration.

    Args:
        config: The configuration object.

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
    public_packages = get_distro_packages(config)
    for package in public_packages.values():
        try:
            package_schema.validate(package)
        except SchemaError as error:
            raise ConfigFileValidationError(package["name"], str(error)) from error


def validate_extra_pip_requirements(config):
    """
    Validate the extra pip requirements in the configuration.

    Args:
        config: The configuration object.

    Raises:
        ConfigFileValidationError: If an extra pip requirement validation fails.
    """
    pip_requirement_schema = Schema(str, len)
    if "OPENEDX_EXTRA_PIP_REQUIREMENTS" in config:
        ep_requirements = config["OPENEDX_EXTRA_PIP_REQUIREMENTS"]
        for requirement in ep_requirements:
            try:
                pip_requirement_schema.validate(requirement)
            except SchemaError as error:
                raise ConfigFileValidationError(requirement, str(error)) from error


def validate_themes(config):
    """
    Validate the themes in the configuration.

    Args:
        config: The configuration object.

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
    if "DISTRO_THEMES" in config:
        for theme in config["DISTRO_THEMES"]:
            try:
                themes_schema.validate(theme)
            except SchemaError as error:
                raise ConfigFileValidationError(theme["name"], str(error)) from error


def validate_theme_settings(config):
    """
    Validate the theme settings in the configuration.

    Args:
        config: The configuration object.

    Raises:
        ConfigFileValidationError: If the theme settings validation fails.
    """
    themes_settings_schema = Schema(
        {
            Optional("DISTRO_THEMES_NAME"): And(list, len),
            Optional("DISTRO_THEME_DIRS"): And(list, len),
            Optional("DISTRO_THEMES_ROOT"): And(str, len),
        },
        ignore_extra_keys=True
    )
    try:
        themes_settings_schema.validate(config)
    except SchemaError as error:
        raise ConfigFileValidationError("Theme settings", str(error)) from error


def validate_extra_files_requirements(config):
    """
    Validate the extra file requirements in the configuration.

    Args:
        config: The configuration object.

    Raises:
        ConfigFileValidationError: If an extra file requirement validation fails.
    """
    extra_files_schema = Schema(
        {
            "files": And(list),
            "path": And(str, len),
        },
    )
    if "INSTALL_EXTRA_FILE_REQUIREMENTS" in config:
        try:
            extra_files_schema.validate(config["INSTALL_EXTRA_FILE_REQUIREMENTS"])
        except SchemaError as error:
            raise ConfigFileValidationError("INSTALL_EXTRA_FILE_REQUIREMENTS", str(error)) from error


def validate_extra_settings(config):
    """
    Validate the extra settings in the configuration.

    Args:
        config: The configuration object.

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
    if "OPENEDX_EXTRA_SETTINGS" in config:
        try:
            extra_settings_schema.validate(config["OPENEDX_EXTRA_SETTINGS"])
        except SchemaError as error:
            raise ConfigFileValidationError("OPENEDX_EXTRA_SETTINGS", str(error)) from error
