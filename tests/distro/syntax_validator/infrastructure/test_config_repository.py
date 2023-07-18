"""
Module for testing the config repository and validation functions list.
"""

from tutordistro.distro.share.domain.config_extra_files_requirements_setting import ConfigExtraFilesRequirementsSetting
from tutordistro.distro.share.domain.config_extra_pip_requirements_setting import ConfigExtraPipRequirementsSetting
from tutordistro.distro.share.domain.config_extra_setting import ConfigExtraSetting
from tutordistro.distro.share.domain.config_packages_setting import ConfigPackagesSetting
from tutordistro.distro.share.domain.config_themes_setting import ConfigThemesSetting
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


def config_setting():
    """
    Returns a list of config settings classes.
    """
    return [
        ConfigExtraFilesRequirementsSetting,
        ConfigExtraPipRequirementsSetting,
        ConfigExtraSetting,
        ConfigPackagesSetting,
        ConfigThemesSetting,
    ]


def config_file_content():
    """
    Returns a dictionary representing the content of a config file.
    """
    return {
        "DISTRO_EOX_TEST_DPKG": {
            "domain": "github.com",
            "index": "git",
            "name": "eox-test",
            "path": "eduNEXT",
            "private": False,
            "protocol": "https",
            "repo": "eox-test",
            "variables": {
                "development": {
                    "EOX_TEST_BACKEND": "eox_test.edxapp_wrapper.backends.test_v1"
                },
                "production": {
                    "EOX_TEST_BACKEND": "eox_test.edxapp_wrapper.backends.test_v1"
                }
            },
            "version": "v1.0.0"
        },
        "DISTRO_EOX_PRIVATE_DPKG": {
            "domain": "github.com",
            "index": "git",
            "name": "eox-private",
            "path": "eduNEXT",
            "private": True,
            "protocol": "ssh",
            "repo": "eox-private",
            "version": "v1.4.0"
        },
        "OPENEDX_EXTRA_PIP_REQUIREMENTS": [
            "eox-test==1.0.0",
            "eox-private==1.4.0",
            "git+https://github.com/eduNEXT/test@v1.0.0#egg=test-xblock==1.0.0",
            "git+https://github.com/eduNEXT/private.git"
        ],
        'DISTRO_THEMES': [
            {
                'domain': 'github.com',
                'name': 'ednx-test-themes',
                'path': 'eduNEXT',
                'protocol': 'ssh',
                'repo': 'ednx-test-themes',
                'version': 'edunext/test.master'
            }
        ],
        'DISTRO_THEMES_NAME': ['test'],
        'DISTRO_THEMES_ROOT': '/test/themes',
        'DISTRO_THEME_DIRS': [
            '/openedx/themes/ednx-test-themes/edx-platform',
            '/openedx/themes/ednx-test-themes/edx-platform/test-generator',
            '/openedx/themes/ednx-test-themes/edx-platform/test-children'
        ],
        'INSTALL_EXTRA_FILE_REQUIREMENTS': {
            'files': [
                '/edunext/base.txt',
                '/nelp/test.txt'
            ],
            'path': './requirements/extra_file/'
        },
        'OPENEDX_EXTRA_SETTINGS': {
            'cms_env': [{'USE_EOX_TEST': True}],
            'lms_env': [
                {'USE_EOX_TEST': True},
                {'ENABLE_EOX_TEST_DERIVE_WORKAROUND': True}
            ],
            'pre_init_lms_tasks': ['./manage.py lms migrate test']
        }
    }


def test_validate_syntax_with_valid_file():
    """
    Test case for validating syntax with a valid config file.
    """
    config_repository = ConfigRepository(config_setting())

    valid = config_repository.validate_syntax(config_file_content())

    assert valid is True


def test_validate_syntax_with_invalid_file():
    """
    Test case for validating syntax with an invalid config file.
    """
    config_repository = ConfigRepository(config_setting())
    config_file_content = {
        "DISTRO_EOX_PRIVATE_DPKG": {
            "index_fail": "git",
            "name": "eox-private",
            "path": "eduNEXT",
            "private": True,
            "protocol": "ssh",
            "repo": "eox-private",
            "version": "v1.4.0"
        },
    }

    invalid = config_repository.validate_syntax(config_file_content)

    assert invalid is False


def test_validate_syntax_without_principal_settings():
    """
    Test case for validating syntax without principal settings.
    """
    config_repository = ConfigRepository(config_setting())

    valid = config_repository.validate_syntax({})

    assert valid is True
