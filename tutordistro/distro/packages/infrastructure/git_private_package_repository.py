from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_repository import PackageRepository


class GitPrivatePackageRepository(PackageRepository):
    def set_as_private(self, name: PackageName) -> None:
        pass

    def clone(self, package: Package, path: str) -> None:
        pass
