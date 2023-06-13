from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist


class InMemoryPackageRepository(CloudPackageRepository):

    def __init__(self, list_repositories: list) -> None:
        self.repositories = list_repositories
    

    def validate(self, package: CloudPackage) -> None:
        if not package.to_url() in self.repositories:
            raise PackageDoesNotExist(f"The package {package.name} or branch doesn't exist or is private")
        