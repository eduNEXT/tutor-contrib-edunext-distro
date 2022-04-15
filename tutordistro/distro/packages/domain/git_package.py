from __future__ import annotations

from tutordistro.distro.packages.domain.git_package_repository_name import GitPackageRepositoryName
from tutordistro.distro.packages.domain.git_package_repository_path import GitPackageRepositoryPath
from tutordistro.distro.packages.domain.git_package_repository_protocol import GitPackageRepositoryProtocol
from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_domain import PackageDomain
from tutordistro.distro.packages.domain.package_index import PackageIndex
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_version import PackageVersion


class GitPackage(Package):
    """
        An python package in a git repository
    """

    def __init__(
        self,
        name: PackageName,
        version: PackageVersion,
        domain: PackageDomain,
        repo: GitPackageRepositoryName,
        protocol: GitPackageRepositoryProtocol,
        path: GitPackageRepositoryPath
    ) -> None:
        self._index = PackageIndex("git")
        self._repo = repo
        self._protocol = protocol
        self._path = path
        super(GitPackage, self).__init__(name=name, version=version, domain=domain, index=self._index)

    @property
    def repo(self):
        return self._repo

    @property
    def protocol(self):
        return self._protocol

    @property
    def path(self):
        return self._path
