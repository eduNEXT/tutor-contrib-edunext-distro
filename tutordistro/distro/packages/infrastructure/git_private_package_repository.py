from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_repository import PackageRepository


class GitPrivatePackageRepository(PackageRepository):
    def clone(self, package: Package, path: str) -> None:
        pass

    def set(self, package: Package) -> None:
        pass
