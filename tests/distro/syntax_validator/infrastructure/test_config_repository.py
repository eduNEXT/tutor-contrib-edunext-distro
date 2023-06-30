import pytest
from tutordistro.distro.share.domain.config_file import ConfigFile
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository


class MockClick:
    def echo(self, error):
        pass


@pytest.fixture
def mock_click(mocker):
    return mocker.patch("click.echo", side_effect=MockClick().echo)


def test_validate_config_with_valid_file(mock_click):
    # Arrange
    config_repository = ConfigRepository()
    config_file = ConfigFile({})

    # Act
    result = config_repository.validate_config(config_file)

    # Assert
    assert result is True
    mock_click.assert_not_called()


def test_validate_config_with_invalid_file(mock_click):
    # Arrange
    config_repository = ConfigRepository()
    config_file = ConfigFile("invalid_config.yml")

    # Act
    result = config_repository.validate_config(config_file)

    # Assert
    assert result is False
    mock_click.assert_called_once()
