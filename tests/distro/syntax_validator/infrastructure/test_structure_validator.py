import pytest
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.syntax_validator.infrastructure.structure_validator import validate_extra_files_requirements, validate_extra_pip_requirements, validate_extra_settings, validate_packages, validate_theme_settings, validate_themes
from schema import SchemaError


def test_validate_packages():
    config = {
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
        }
    }
    assert_no_exception(lambda: validate_packages(config))

def test_validate_extra_pip_requirements():
    config = {
        "OPENEDX_EXTRA_PIP_REQUIREMENTS": [
            "eox-test==1.0.0",
            "eox-private==1.4.0",
            "git+https://github.com/eduNEXT/test@v1.0.0#egg=test-xblock==1.0.0",
            "git+https://github.com/eduNEXT/private.git"
        ]
    }
    assert_no_exception(lambda: validate_extra_pip_requirements(config))

def test_validate_themes():
    config = {
        'DISTRO_THEMES': [
            {
                'domain': 'github.com',
                'name': 'ednx-test-themes',
                'path': 'eduNEXT',
                'protocol': 'ssh',
                'repo': 'ednx-test-themes',
                'version': 'edunext/test.master'
            }
        ]
    }
    assert_no_exception(lambda: validate_themes(config))

def test_validate_theme_settings():
    config = {
        'DISTRO_THEMES_NAME': ['test'],
        'DISTRO_THEMES_ROOT': '/test/themes',
        'DISTRO_THEME_DIRS': [
            '/openedx/themes/ednx-test-themes/edx-platform',
            '/openedx/themes/ednx-test-themes/edx-platform/test-generator',
            '/openedx/themes/ednx-test-themes/edx-platform/test-children'
        ]
    }
    assert_no_exception(lambda: validate_theme_settings(config))

def test_validate_extra_files_requirements():
    config = {
        'INSTALL_EXTRA_FILE_REQUIREMENTS': {
            'files': [
                '/edunext/base.txt',
                '/nelp/test.txt'
            ],
            'path': './requirements/extra_file/'
        }
    }
    assert_no_exception(lambda: validate_extra_files_requirements(config))

def test_validate_extra_settings():
    config = {
        'OPENEDX_EXTRA_SETTINGS': {
            'cms_env': [{'USE_EOX_TEST': True}],
            'lms_env': [
                {'USE_EOX_TEST': True},
                {'ENABLE_EOX_TEST_DERIVE_WORKAROUND': True}
            ],
            'pre_init_lms_tasks': ['./manage.py lms migrate test']
        }
    }
    assert_no_exception(lambda: validate_extra_settings(config))

def assert_no_exception(func):
    try:
        func()
    except ConfigFileValidationError as e:
        pytest.fail(f"ConfigFileValidationError occurred: {str(e)}")
    except SchemaError as e:
        pytest.fail(f"SchemaError occurred: {str(e)}")
