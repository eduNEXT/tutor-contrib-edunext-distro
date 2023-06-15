"""
This module provides the ExtraPipRequirementsUrlValidator class for validating
extra pip requirements URLs.
"""


from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository


class ExtraPipRequirementsUrlValidator:  # pylint: disable=too-few-public-methods
    """
    Validator class for validating extra pip requirements URLs.

    It uses a CloudPackageRepository to validate the package represented by the URL.
    """
    def __init__(self, repository: CloudPackageRepository) -> None:
        self.repository = repository

    def __call__(
        self,
        url: str
    ) -> None:
        if CloudPackage.is_valid_requirement(url):
            git_package = CloudPackage.from_string(url)
            self.repository.validate(package=git_package)
