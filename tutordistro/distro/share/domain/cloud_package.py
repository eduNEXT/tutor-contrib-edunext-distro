"""
This module provides the CloudPackage class representing a cloud package.

The CloudPackage class is used to parse and manipulate URLs representing cloud-based packages.
"""


from __future__ import annotations

import re
from urllib.parse import urlparse

from tutordistro.distro.share.domain.package import Package


class CloudPackage:
    """
    Representation of a cloud package.

    The CloudPackage class is used to parse and manipulate URLs representing cloud-based packages.
    """
    domain: str | None = None
    name: str | None = None
    version: str | None = None
    protocol: str | None = None
    path: str | None = None

    def __init__(self, domain: str, name: str, version: str, protocol: str, path: str) -> None:  # pylint: disable=too-many-arguments
        self.domain = domain
        self.name = name
        self.version = version
        self.protocol = protocol
        self.path = path

    @staticmethod
    def is_valid_requirement(url) -> bool:
        """
        Check if the provided URL is a valid requirement.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is a valid requirement, False otherwise.
        """
        pattern = r"git\+(https?://\S+?)(?:#|$)"
        result = re.search(pattern, url)
        return bool(result)

    @staticmethod
    def __parse_url(url) -> CloudPackage:
        version: str = ''

        pattern = r"git\+(https?://\S+?)(?:#|$)"
        found_package_url = re.search(pattern, url).group(1)
        github_url = found_package_url.replace('@', '/tree/').replace('.git', '')

        parsed_url = urlparse(github_url)
        split_path = parsed_url.path.split('/')

        protocol = parsed_url.scheme
        domain = parsed_url.netloc
        org_path = split_path[1]
        package_name = split_path[2]

        if '/tree/' in github_url:
            version = github_url.split('/tree/')[-1]  # This is the branch name or tag

        return CloudPackage(
            domain=domain,
            name=package_name,
            version=version,
            protocol=protocol,
            path=org_path
        )

    @staticmethod
    def __parse_package(package: Package) -> CloudPackage:
        return CloudPackage(
            path=package.extra["path"],
            protocol=package.extra["protocol"],
            domain=package.domain,
            version=package.version,
            name=package.extra["repo"]
        )

    @staticmethod
    def from_string(url: str) -> CloudPackage:
        """
        Create a CloudPackage object from the provided URL string.

        Args:
            url (str): The URL string representing the cloud package.

        Returns:
            CloudPackage: The created CloudPackage object.
        """
        return CloudPackage.__parse_url(url=url)

    @staticmethod
    def from_package(package: Package) -> CloudPackage:
        """
        Create a CloudPackage object from the provided Package object.

        Args:
            package (Package): The Package object representing the cloud package.

        Returns:
            CloudPackage: The created CloudPackage object.
        """
        return CloudPackage.__parse_package(package=package)

    def to_url(self) -> str:
        """
        Convert the CloudPackage object to a URL string.

        Returns:
            str: The URL string representing the CloudPackage.
        """
        version_url = f"/tree/{self.version}" if self.version != "" else ""
        return f"{self.protocol}://{self.domain}/{self.path}/{self.name}{version_url}"

    def __str__(self) -> str:
        return self.to_url()
