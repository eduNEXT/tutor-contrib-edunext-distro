from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_repository import PackageRepository


class PackageCloner:
    def __init__(self, repository: PackageRepository) -> None:
        self.repository = repository

    def __call__(self, package: Package, path: str) -> None:
        self.repository.clone(package=package, path=path)
