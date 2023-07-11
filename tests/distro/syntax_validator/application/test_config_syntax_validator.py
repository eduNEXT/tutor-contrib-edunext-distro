"""
Module for testing the ConfigSyntaxValidator class.
"""
from unittest.mock import Mock, patch

import pytest

from tests.distro.syntax_validator.infrastructure.test_config_repository import config_setting
from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.syntax_validator.application.config_syntax_validator import ConfigSyntaxValidator
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


@pytest.fixture
def config_repository():
    """
    Fixture for creating a ConfigRepository object.
    """
    return ConfigRepository(config_setting())


@pytest.fixture
def config_syntax_validator(config_repository):
    """
    Fixture for creating a ConfigSyntaxValidator object.
    """
    return ConfigSyntaxValidator(config_repository)


def test_execute(config_syntax_validator):
    """
    Test case for the execute method of ConfigSyntaxValidator class.
    """
    file_path_mock = Mock()
    config_syntax_validator.repository.validate_syntax = Mock(return_value=True)

    with patch.object(ConfigFile, 'config_file', return_value=file_path_mock):
        result = config_syntax_validator.execute(file_path_mock)

    assert isinstance(result, bool)
    config_syntax_validator.repository.validate_syntax.assert_called_once_with(file_path_mock)
