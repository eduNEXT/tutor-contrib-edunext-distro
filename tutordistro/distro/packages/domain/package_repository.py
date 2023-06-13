"""
Distro package repository.
"""

from abc import ABC, abstractmethod

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_name import PackageName


class PackageRepository(ABC):
    """
    Abstract base class for package repositories.

    This class defines the interface for package repositories, which are responsible for
    cloning packages and setting them as private.

    Concrete implementations of package repositories should inherit from this class and
    provide implementations for the `clone` and `set_as_private` methods.
    """

    @abstractmethod
    def clone(self, package: Package, path: str) -> None:
        """
        Clone a package.

        This method should clone the specified package to the specified path.

        Args:
            package (Package): The package to clone.
            path (str): The path to clone the package to.
        """

    @abstractmethod
    def set_as_private(self, name: PackageName, file_path: str) -> None:
        """
        Set a package as private.

        This method should mark the specified package as private, using the specified file path.

        Args:
            name (PackageName): The name of the package to set as private.
            file_path (str): The file path to use for marking the package as private.
        """
