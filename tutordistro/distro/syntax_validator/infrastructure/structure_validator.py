from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.utils.packages import get_distro_packages
from schema import Schema, And, Optional, Or, SchemaError


def validate_packages(config):
    PACKAGE_SCHEMA = Schema(
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
            PACKAGE_SCHEMA.validate(package)
        except SchemaError as e:
            raise ConfigFileValidationError(package["name"], str(e))


def validate_extra_pip_requirements(config):
    PIP_REQUIREMENT_SCHEMA = Schema(str, len)
    if "OPENEDX_EXTRA_PIP_REQUIREMENTS" in config:
        ep_requirements = config["OPENEDX_EXTRA_PIP_REQUIREMENTS"]
        for requirement in ep_requirements:
            try:
                PIP_REQUIREMENT_SCHEMA.validate(requirement)
            except SchemaError as e:
                raise ConfigFileValidationError(requirement, str(e))


def validate_themes(config):
    THEME_SCHEMA = Schema(
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
                THEME_SCHEMA.validate(theme)
            except SchemaError as e:
                raise ConfigFileValidationError(theme["name"], str(e))

def validate_theme_settings(config):
    THEMES_SETTINGS_SCHEMA = Schema(
        {
            Optional("DISTRO_THEMES_NAME"): And(list, len),
            Optional("DISTRO_THEME_DIRS"): And(list, len),
            Optional("DISTRO_THEMES_ROOT"): And(str, len),
        },
        ignore_extra_keys=True
    )
    try:
        THEMES_SETTINGS_SCHEMA.validate(config)
    except SchemaError as e:
        raise ConfigFileValidationError("Theme settings", str(e))


def validate_extra_files_requirements(config):
    EXTRA_FILES_SCHEMA = Schema(
        {
            "files": And(list),
            "path": And(str, len),
        },
    )
    if "INSTALL_EXTRA_FILE_REQUIREMENTS" in config:
        try:
            EXTRA_FILES_SCHEMA.validate(config["INSTALL_EXTRA_FILE_REQUIREMENTS"])
        except SchemaError as e:
            raise ConfigFileValidationError("INSTALL_EXTRA_FILE_REQUIREMENTS", str(e))

def validate_extra_settings(config):
    EXTRA_SETTINGS_SCHEMA = Schema(
        {
            Optional("cms_env"): And(list),
            Optional("lms_env"): And(list),
            Optional("pre_init_lms_tasks"): And(list),
        },
    )
    if "OPENEDX_EXTRA_SETTINGS" in config:
        try:
            EXTRA_SETTINGS_SCHEMA.validate(config["OPENEDX_EXTRA_SETTINGS"])
        except SchemaError as e:
            raise ConfigFileValidationError("OPENEDX_EXTRA_SETTINGS", str(e))
