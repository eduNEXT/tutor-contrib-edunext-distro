"""
This module provides the abstract base class for cloud package repositories.
"""


from abc import ABC, abstractmethod

from tutordistro.distro.share.domain.cloud_package import CloudPackage


class CloudPackageRepository(ABC):
    """
    Abstract base class for cloud package repositories.

    The CloudPackageRepository class defines the interface for a cloud package repository,
    which provides the ability to validate cloud packages.
    """

    @abstractmethod
    def validate(self, package: CloudPackage) -> None:
        """
        Validate a cloud package.

        This method is responsible for validating a cloud package in the repository.

        Args:
            package (CloudPackage): The cloud package to validate.

        Raises:
            NotImplementedError: This method should be implemented in concrete subclasses.
        """
