from tutordistro.distro.share.domain.package import Package
from tutordistro.distro.share.domain.package_domain import PackageDomain
from tutordistro.distro.share.domain.package_name import PackageName
from tutordistro.distro.share.domain.package_version import PackageVersion
from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository


class DPKGUrlValidator:
    def __init__(self, repository: CloudPackageRepository) -> None:
        self.repository = repository

    def __call__(
        self,
        name: str,
        version: str,
        domain: str,
        extra: dict = None
    ) -> None:
        name = PackageName(name)
        version = PackageVersion(version)
        domain = PackageDomain(domain)
        package = Package(name=name, version=version, domain=domain, extra=extra if extra else {})
        git_package = CloudPackage.from_package(package=package)

        self.repository.validate(package=git_package)
