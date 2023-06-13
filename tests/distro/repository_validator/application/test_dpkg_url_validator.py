import pytest
from tests.distro.repository_validator.infrastructure.in_memory_package_repository import InMemoryPackageRepository
from tutordistro.distro.repository_validator.application.dpkg_url_validator import DPKGUrlValidator
from tutordistro.distro.repository_validator.application.extra_pip_requirements_url_validator import ExtraPipRequirementsUrlValidator
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist

# Test case for validator when the repository exists
def test_validator_when_repo_exists():
    # Given
    repository = InMemoryPackageRepository(["https://github.com/test/testrepo/tree/2.0.1"])
    validator = DPKGUrlValidator(repository=repository)

    validator(
        name="ednx_package",
        version="2.0.1",
        domain="github.com",
        extra={"path": "test",
                "protocol": "https",
                "repo": "testrepo"}
    )

# Test case for validator when the repository does not exist
def test_validator_when_repo_does_not_exists():
    with pytest.raises(PackageDoesNotExist) as package_error:
        # Given
        repository = InMemoryPackageRepository([])
        validator = DPKGUrlValidator(repository=repository)
        # When
        validator(
            name="ednx_package",
            version="2.0.1",
            domain="github.com",
            extra={"path": "test",
                    "protocol": "https",
                    "repo": "testrepo"}
        )

    # Then
    assert package_error.type is PackageDoesNotExist

# Test case for validator when extra pip requirements exist
def test_validator_when_extra_pip_requeriments_exists():
    #Given
    repository = InMemoryPackageRepository(["https://github.com/eduNEXT/edx_xblock_scorm/tree/v2.0.0"])
    validator = ExtraPipRequirementsUrlValidator(repository=repository)
    validator(
        url="git+https://github.com/eduNEXT/edx_xblock_scorm@v2.0.0#egg=scormxblock-xblock==2.0.0"
    )

# Test case for validator when extra pip requirements do not exist
def test_validator_when_extra_pip_requeriments_does_not_exists():
    with pytest.raises(PackageDoesNotExist) as package_error:
        #Given
        repository = InMemoryPackageRepository([])
        validator = ExtraPipRequirementsUrlValidator(repository=repository)
        # When
        validator(
            url="git+https://github.com/eduNEXT/edx_xblock_scorm@v2.0.0#egg=scormxblock-xblock==2.0.0"
        )
    # Then
    assert package_error.type is PackageDoesNotExist
