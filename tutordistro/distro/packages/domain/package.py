from __future__ import annotations

from abc import ABC

from tutordistro.distro.packages.domain.package_version import PackageVersion
from tutordistro.distro.packages.domain.package_domain import PackageDomain
from tutordistro.distro.packages.domain.package_index import PackageIndex
from tutordistro.distro.packages.domain.package_name import PackageName


class Package(ABC):
    """
        An python package
    """

    def __init__(
        self,
        name: PackageName,
        index: PackageIndex,
        domain: PackageDomain,
        version: PackageVersion
    ) -> None:
        self._name = name
        self._index = index
        self._domain = domain
        self._version = version

    @property
    def name(self) -> PackageName:
        return self._name

    @property
    def index(self) -> PackageIndex:
        return self._index

    @property
    def domain(self) -> PackageDomain:
        return self._domain

    @property
    def version(self) -> PackageVersion:
        return self._version
