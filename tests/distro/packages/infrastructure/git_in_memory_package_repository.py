from typing import Dict

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.packages.share.domain.clone_exception import CloneException


class GitInMemoryPackageRepository(PackageRepository):
    repos = {}

    def __init__(self, repos: Dict = {}):
        self.repos = repos

    def clone(self, package: Package, path: str) -> None:
        if self.repos and package.name in self.repos[path]:
            raise CloneException

        self.repos.update({
            path: [package.name]
        })
