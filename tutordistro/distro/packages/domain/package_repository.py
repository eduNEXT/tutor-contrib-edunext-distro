from abc import ABC, abstractmethod

from tutordistro.distro.packages.domain.package import Package


class PackageRepository(ABC):

    @abstractmethod
    def clone(self, package: Package, path: str) -> None:
        pass
