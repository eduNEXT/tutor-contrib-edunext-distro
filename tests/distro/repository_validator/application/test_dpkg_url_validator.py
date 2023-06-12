import pytest

from tutordistro.distro.repository_validator.application.dpkg_url_validator import DPKGUrlValidator


def test_validator_when_repo_exists():
    # Given
    repository = ""
    validator = DPKGUrlValidator(repository=repository)

    validator(
        name="ednx_package",
        version="v1.0.0",

    )

    #with PackageDoesNotExist: