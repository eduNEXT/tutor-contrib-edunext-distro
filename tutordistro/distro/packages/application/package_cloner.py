"""
Package cloner process.
"""

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_domain import PackageDomain
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.packages.domain.package_version import PackageVersion


class PackageCloner:  # pylint: disable=too-few-public-methods
    """
    Package cloner process.

    This class is responsible for cloning a package using a given package repository.

    Args:
        repository (PackageRepository): The package repository used for cloning.

    Attributes:
        repository (PackageRepository): The package repository used for cloning.
    """

    def __init__(self, repository: PackageRepository) -> None:
        self.repository = repository

    def __call__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        version: str,
        domain: str,
        path: str,
        extra: dict = None
    ) -> None:
        """
        Clone a package to the specified path.

        Args:
            name (str): The name of the package.
            version (str): The version of the package.
            domain (str): The domain of the package.
            path (str): The path to clone the package.
            extra (dict, optional): Extra metadata associated with the package. Defaults to None.
        """
        name = PackageName(name)
        version = PackageVersion(version)
        domain = PackageDomain(domain)
        package = Package(name=name, version=version, domain=domain, extra=extra if extra else {})

        self.repository.clone(package=package, path=path)
