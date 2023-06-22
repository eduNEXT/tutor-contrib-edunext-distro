"""
Package module.
"""

from __future__ import annotations

from abc import ABC
from typing import Dict

from tutordistro.distro.share.domain.package_domain import PackageDomain
from tutordistro.distro.share.domain.package_name import PackageName
from tutordistro.distro.share.domain.package_version import PackageVersion


class Package(ABC):
    """
    Abstract base class for a package.

    This class represents a package with a name, domain, version, and additional extra metadata.

    Args:
        name (PackageName): The name of the package.
        domain (PackageDomain): The domain of the package.
        version (PackageVersion): The version of the package.
        extra (Dict): Extra metadata associated with the package.
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
        """
        Get the name of the package.

        Returns:
            PackageName: The name of the package.
        """
        return self._name

    @property
    def domain(self) -> PackageDomain:
        """
        Get the domain of the package.

        Returns:
            PackageDomain: The domain of the package.
        """
        return self._domain

    @property
    def version(self) -> PackageVersion:
        """
        Get the version of the package.

        Returns:
            PackageVersion: The version of the package.
        """
        return self._version

    @property
    def extra(self) -> Dict:
        """
        Get the extra metadata of the package.

        Returns:
            Dict: Extra metadata associated with the package.
        """
        return self._extra
