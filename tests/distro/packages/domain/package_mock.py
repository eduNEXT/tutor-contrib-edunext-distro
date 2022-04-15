from tutordistro.distro.packages.domain.git_package import GitPackage
from tutordistro.distro.packages.domain.git_package_repository_name import GitPackageRepositoryName
from tutordistro.distro.packages.domain.git_package_repository_path import GitPackageRepositoryPath
from tutordistro.distro.packages.domain.git_package_repository_protocol import GitPackageRepositoryProtocol
from tutordistro.distro.packages.domain.package_domain import PackageDomain
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_version import PackageVersion


class GitPackageMock:
    def __init__(
        self,
        name: str = None,
        version: str = None,
        domain: str = None,
        repo: str = None,
        protocol: str = None,
        path: str = None
    ) -> None:
        self._name = PackageName(name if name else "eox-test")
        self._version = PackageVersion(version if version else "v1.0.0")
        self._domain = PackageDomain(domain if domain else "github.com")
        self._protocol = GitPackageRepositoryProtocol(protocol if protocol else "ssh")
        self._path = GitPackageRepositoryPath(path if path else "eduNEXT")
        self._repo = GitPackageRepositoryName(repo if repo else "eox-test")

    def create(self):
        return GitPackage(
            name=self._name,
            version=self._version,
            domain=self._domain,
            repo=self._repo,
            protocol=self._protocol,
            path=self._path
        )
