"""Package repository interface."""
from abc import ABC, abstractmethod

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_name import PackageName


class PackageRepository(ABC):
    """Package repository interface."""
    @abstractmethod
    def clone(self, package: Package, path: str) -> None:
        """Method to clone packages."""

    @abstractmethod
    def set_as_private(self, name: PackageName, file_path: str) -> None:
        """Method to set a package as private."""
