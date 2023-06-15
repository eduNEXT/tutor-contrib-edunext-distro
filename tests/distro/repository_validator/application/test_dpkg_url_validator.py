"""
pytest module for testing the validators in the
tutordistro.distro.repository_validator.application package.

This module contains pytest test cases for the various validators in the
tutordistro.distro.repository_validator.application package.

Test Cases:
- test_validator_when_repo_exists: Test case for the validator when the repository exists.
- test_validator_when_repo_does_not_exists: Test case for the validator when the
repository does not exist.
- test_validator_when_extra_pip_requeriments_exists: Test case for the validator
when extra pip requirements exist.
- test_validator_when_extra_pip_requeriments_does_not_exists: Test case for the
validator when extra pip requirements do not exist.
"""


import pytest
from tests.distro.repository_validator.infrastructure.in_memory_package_repository \
    import InMemoryPackageRepository
from tutordistro.distro.repository_validator.application.dpkg_url_validator import DPKGUrlValidator
from tutordistro.distro.repository_validator.application.extra_pip_requirements_url_validator \
    import ExtraPipRequirementsUrlValidator
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist


# Test case for validator when the repository exists
def test_validator_when_repo_exists():
    """
    Test case for the validator when the repository exists.

    This test case checks the behavior of the validator when the repository exists.
    It validates that the validator does not raise any exceptions.

    Steps:
    1. Create an instance of InMemoryPackageRepository with a non-empty repository URL list.
    2. Create an instance of DPKGUrlValidator with the repository.
    3. Invoke the validator with the required parameters.
    """
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
    """
    Test case for the validator when the repository does not exist.

    This test case checks the behavior of the validator when the repository does not exist.
    It validates that the validator raises a PackageDoesNotExist exception.

    Steps:
    1. Create an instance of InMemoryPackageRepository with an empty repository URL list.
    2. Create an instance of DPKGUrlValidator with the repository.
    3. Invoke the validator with the required parameters.
    4. Check that the validator raises a PackageDoesNotExist exception.
    """
    with pytest.raises(PackageDoesNotExist) as package_error:
        repository = InMemoryPackageRepository([])
        validator = DPKGUrlValidator(repository=repository)

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
    """
    Test case for the validator when extra pip requirements exist.

    This test case checks the behavior of the validator when extra pip requirements exist.
    It validates that the validator does not raise any exceptions.

    Steps:
    1. Create an instance of InMemoryPackageRepository with a non-empty repository URL list.
    2. Create an instance of ExtraPipRequirementsUrlValidator with the repository.
    3. Invoke the validator with a valid URL.
    """
    repository = InMemoryPackageRepository(
        ["https://github.com/eduNEXT/edx_xblock_scorm/tree/v2.0.0"]
    )
    validator = ExtraPipRequirementsUrlValidator(repository=repository)
    validator(
        url="git+https://github.com/eduNEXT/edx_xblock_scorm@v2.0.0#egg=scormxblock-xblock==2.0.0"
    )


def test_validator_when_extra_pip_requeriments_does_not_exists():
    """
    Test case for the validator when extra pip requirements do not exist.

    This test case checks the behavior of the validator when extra pip requirements do not exist.
    It validates that the validator raises a PackageDoesNotExist exception.

    Steps:
    1. Create an instance of InMemoryPackageRepository with an empty repository URL list.
    2. Create an instance of ExtraPipRequirementsUrlValidator with the repository.
    3. Invoke the validator with an invalid URL.
    4. Check that the validator raises a PackageDoesNotExist exception.
    """
    with pytest.raises(PackageDoesNotExist) as package_error:
        repository = InMemoryPackageRepository([])
        validator = ExtraPipRequirementsUrlValidator(repository=repository)

        validator(
            url="git+https://github.com/eduNEXT/edx_xblock_scorm@v2.0.0"
            "#egg=scormxblock-xblock==2.0.0"
        )

    assert package_error.type is PackageDoesNotExist
