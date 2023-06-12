import requests

from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist


class GitPackageRepository(CloudPackageRepository):
    def validate(self, package: CloudPackage) -> None:
        response = requests.get(package.to_url())
        if response.status_code != 200:
            raise PackageDoesNotExist(f"The package {package.name} or branch doesn't exist or is private")
