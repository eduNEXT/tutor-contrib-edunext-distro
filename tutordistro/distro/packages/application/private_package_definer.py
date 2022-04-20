from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_repository import PackageRepository


class PrivatePackageDefiner:
    def __init__(self, repository: PackageRepository) -> None:
        self.repository = repository

    def __call__(
        self,
        name: str,
        file_path: str
    ) -> None:
        name = PackageName(name)
        self.repository.set_as_private(name=name, file_path=file_path)
