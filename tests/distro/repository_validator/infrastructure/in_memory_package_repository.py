"""
Module: InMemoryPackageRepository
This module defines the InMemoryPackageRepository class, which is an implementation
of the CloudPackageRepository interface. It provides an in-memory storage for
repositories and implements the validate method to check if a
package exists in the stored repositories.
"""


from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist


class InMemoryPackageRepository(CloudPackageRepository):  # pylint: disable=too-few-public-methods
    """
    InMemoryPackageRepository class implements the CloudPackageRepository
    interface and provides an in-memory storage for repositories.
    It allows validating if a package exists in the stored repositories.
    """
    def __init__(self, list_repositories: list) -> None:
        self.repositories = list_repositories

    def validate(self, package: CloudPackage) -> None:
        if not package.to_url() in self.repositories:
            raise PackageDoesNotExist(f"The package {package.name} "
                                      "or branch doesn't exist or is private")
