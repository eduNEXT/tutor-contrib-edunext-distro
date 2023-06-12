from __future__ import annotations
import re
from urllib.parse import urlparse

from tutordistro.distro.share.domain.package import Package


class CloudPackage:
    domain: str | None = None
    name: str | None = None
    version: str | None = None
    protocol: str | None = None
    path: str | None = None

    def __init__(self, domain: str, name: str, version: str, protocol: str, path: str) -> None:
        self.domain = domain
        self.name = name
        self.version = version
        self.protocol = protocol
        self.path = path

    @staticmethod
    def is_valid_requirement(url) -> bool:
        pattern = r"git\+(https?://\S+?)(?:#|$)"
        result = re.search(pattern, url)
        return True if result else False

    @staticmethod
    def __parse_url(url) -> CloudPackage:
        version: str = ""

        pattern = r"git\+(https?://\S+?)(?:#|$)"
        result = re.search(pattern, url)
        url = result.group(1).replace('@', '/tree/').replace('.git', '')

        parsed_url = urlparse(url)

        protocol = parsed_url.scheme
        domain = parsed_url.netloc
        path = parsed_url.path
        partes_path = path.split('/')
        name = partes_path[2]

        if '/tree/' in url:
            version = partes_path[-1]

        path = partes_path[1]

        return CloudPackage(
            domain=domain,
            name=name,
            version=version,
            protocol=protocol,
            path=path
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
        return CloudPackage.__parse_url(url=url)

    @staticmethod
    def from_package(package: Package) -> CloudPackage:
        return CloudPackage.__parse_package(package=package)

    def to_url(self) -> str:
        version_url = f"/tree/{self.version}" if self.version != "" else ""
        return f"{self.protocol}://{self.domain}/{self.path}/{self.name}{version_url}"

    def __str__(self) -> str:
        return self.to_url()
