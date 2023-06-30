"""
This module provides the GitPackageRepository class, which is a specific implementation
of the CloudPackageRepository.
It interacts with a Git repository to validate a CloudPackage.
"""


import requests

from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist


class GitPackageRepository(CloudPackageRepository):
    """
    Repository class for validating CloudPackages using a Git repository.

    It inherits from CloudPackageRepository and provides the implementation for
    the validation method.
    """
    def validate(self, package: CloudPackage) -> None:
        response = requests.get(package.to_url(), timeout=5)
        if response.status_code != 200:
            raise PackageDoesNotExist(f"The package {package.name} or branch doesn't exist or is private")
