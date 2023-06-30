import pytest
from tutordistro.distro.syntax_validator.application.validate_config_use_case import ValidateConfigUseCase
from tutordistro.distro.syntax_validator.infrastructure.config_repository import ConfigRepository
from tutordistro.distro.share.domain.config_file_validation_error import ConfigFileValidationError

class MockConfigRepository(ConfigRepository):
    def validate_config(self, config_file):
        # Simulate validation logic
        if config_file.file_path == "valid_config.yml":
            return True
        else:
            raise ConfigFileValidationError("Invalid configuration file.", "Schema error")

def test_execute_with_valid_config():
    # Arrange
    mock_repository = MockConfigRepository()
    use_case = ValidateConfigUseCase(mock_repository)
    file_path = "valid_config.yml"

    # Act
    result = use_case.execute(file_path)

    # Assert
    assert result is True

def test_execute_with_invalid_config():
    # Arrange
    mock_repository = MockConfigRepository()
    use_case = ValidateConfigUseCase(mock_repository)
    file_path = "invalid_config.yml"

    # Act and Assert
    with pytest.raises(ConfigFileValidationError):
        use_case.execute(file_path)
