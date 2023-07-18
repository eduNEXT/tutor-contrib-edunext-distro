"""
Private package denifer process.
"""

from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.share.domain.package_name import PackageName


class PrivatePackageDefiner:
    """
    Private package definer process.

    This class is responsible for setting a package as private in the package repository.

    Args:
        repository (PackageRepository): The package repository used for defining private packages.

    Attributes:
        repository (PackageRepository): The package repository used for defining private packages.
    """

    def __init__(self, repository: PackageRepository) -> None:
        self.repository = repository

    def __call__(
        self,
        name: str,
        file_path: str
    ) -> None:
        """
        Define a package as private.

        Args:
            name (str): The name of the package.
            file_path (str): The file path of the package.
        """
        name = PackageName(name)
        self.repository.set_as_private(name=name, file_path=file_path)
