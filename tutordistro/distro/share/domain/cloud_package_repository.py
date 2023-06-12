from abc import ABC, abstractmethod

from tutordistro.distro.share.domain.cloud_package import CloudPackage


class CloudPackageRepository(ABC):

    @abstractmethod
    def validate(self, package: CloudPackage) -> None:
        pass

