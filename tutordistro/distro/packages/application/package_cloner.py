from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_domain import PackageDomain
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.packages.domain.package_version import PackageVersion


class PackageCloner:
    def __init__(self, repository: PackageRepository) -> None:
        self.repository = repository

    def __call__(
        self,
        name: str,
        version: str,
        domain: str,
        path: str,
        extra: dict = None
    ) -> None:
        name = PackageName(name)
        version = PackageVersion(version)
        domain = PackageDomain(domain)
        package = Package(name=name, version=version, domain=domain, extra=extra if extra else {})

        self.repository.clone(package=package, path=path)
