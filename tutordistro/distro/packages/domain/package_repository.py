from abc import ABC, abstractmethod

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_name import PackageName


class PackageRepository(ABC):

    @abstractmethod
    def clone(self, package: Package, path: str) -> None:
        pass

    @abstractmethod
    def set_as_private(self, name: PackageName) -> None:
        pass
