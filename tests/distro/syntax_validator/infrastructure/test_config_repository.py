"""
Module for testing the config repository and validation functions.
"""

import pytest

from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


class MockClick:
    """
    Mock class for Click.
    """
    def echo(self, error):
        """
        Mock echo method.
        """


@pytest.fixture
def mock_click(mocker):
    """
    Fixture for mocking the click.echo function.
    Returns a patched version of click.echo that uses MockClick's echo method.
    """
    return mocker.patch("click.echo", side_effect=MockClick().echo)


def test_validate_config_with_valid_file(mock_click):
    """
    Test the validate_config method of ConfigRepository with a valid config file.
    """
    # Arrange
    config_repository = ConfigRepository()
    config_file = ConfigFile({})

    # Act
    result = config_repository.validate_config(config_file)

    # Assert
    assert result is True
    mock_click.assert_not_called()


def test_validate_config_with_invalid_file(mock_click):
    """
    Test the validate_config method of ConfigRepository with an invalid config file.
    """
    # Arrange
    config_repository = ConfigRepository()
    config_file = ConfigFile("invalid_config.yml")

    # Act
    result = config_repository.validate_config(config_file)

    # Assert
    assert result is False
    mock_click.assert_called_once()
