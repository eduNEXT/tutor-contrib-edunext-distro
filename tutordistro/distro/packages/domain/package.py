"""Package."""
from __future__ import annotations

from abc import ABC
from typing import Dict

from tutordistro.distro.packages.domain.package_version import PackageVersion
from tutordistro.distro.packages.domain.package_domain import PackageDomain
from tutordistro.distro.packages.domain.package_name import PackageName


class Package(ABC):
    """
        An python package
    """

    def __init__(
        self,
        name: PackageName,
        domain: PackageDomain,
        version: PackageVersion,
        extra: Dict
    ) -> None:
        self._name = name
        self._domain = domain
        self._version = version
        self._extra = extra

    @property
    def name(self) -> PackageName:
        """name of the package"""
        return self._name

    @property
    def domain(self) -> PackageDomain:
        """domain of the package"""
        return self._domain

    @property
    def version(self) -> PackageVersion:
        """version of the package"""
        return self._version

    @property
    def extra(self) -> Dict:
        """extra data of the package"""
        return self._extra
