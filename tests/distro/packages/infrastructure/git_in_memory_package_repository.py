from typing import Dict

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_does_not_exist import PackageDoesNotExist
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.packages.share.domain.clone_exception import CloneException


class GitInMemoryPackageRepository(PackageRepository):
    paths = {
        "requirements": []
    }
    private_file = []

    def __init__(self, paths: Dict = None):
        if paths:
            self.paths = paths

    def clone(self, package: Package, path: str) -> None:
        if path in self.paths and package.name in self.paths[path]:
            raise CloneException

        self.paths.update({
            f"{path}": [package.name]
        })

    def set_as_private(self, name: PackageName, file_path: str) -> None:
        if name not in self.paths[file_path]:
            raise PackageDoesNotExist

        self.private_file.append(name)
