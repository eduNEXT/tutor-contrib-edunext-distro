"""
This module provides the GitPackageRepository class, which is a specific implementation
of the CloudPackageRepository.
It interacts with a Git repository to validate a CloudPackage.
"""


from __future__ import annotations

import subprocess
from typing import Optional

from tutordistro.distro.share.domain.cloud_package import CloudPackage
from tutordistro.distro.share.domain.cloud_package_repository import CloudPackageRepository
from tutordistro.distro.share.domain.package_does_not_exist import PackageDoesNotExist


class GitPackageRepository(CloudPackageRepository):
    """
    Repository class for validating CloudPackages using a Git repository.

    This class inherits from CloudPackageRepository and provides the implementation for
    the validation method. It verifies the existence of the repository and checks
    if the specified branch or tag exists.
    """
    def validate(self, package: CloudPackage) -> None:
        package_url = package.to_url()
        repo_url, version_name = self._parse_package_url(package_url)

        self._verify_repository_exists(repo_url)
        if version_name:
            self._verify_version_exists(repo_url, version_name)

    def _parse_package_url(self, package_url: str) -> tuple[str, Optional[str]]:
        """
        Parse the package URL to extract the repository URL and the version name.

        Args:
            package_url (str): The full URL of the package.

        Returns:
            tuple: A tuple containing the repository URL and the version name (branch/tag).
        """
        split_url = package_url.split('/tree/')
        repo_url = split_url[0]
        version_name = split_url[1] if len(split_url) > 1 else None
        return repo_url, version_name

    def _verify_repository_exists(self, repo_url: str) -> None:
        """
        Verify that the repository exists.

        Args:
            repo_url (str): The URL of the repository.

        Raises:
            PackageDoesNotExist: If the repository does not exist or is private.
        """
        result = subprocess.run(
            ['git', 'ls-remote', repo_url],
            capture_output=True, text=True, check=False
        )
        if result.returncode != 0:
            raise PackageDoesNotExist(f'The package "{repo_url}" does not exist or is private')

    def _verify_version_exists(self, repo_url: str, version_name: str) -> None:
        """
        Verify that the branch or tag exists in the repository.

        Args:
            repo_url (str): The URL of the repository.
            version_name (str): The branch or tag name to verify.

        Raises:
            PackageDoesNotExist: If neither the branch nor the tag exists.
        """
        branch_result = subprocess.run(
            ['git', 'ls-remote', '--heads', repo_url, version_name],
            capture_output=True, text=True, check=False
        )
        tag_result = subprocess.run(
            ['git', 'ls-remote', '--tags', repo_url, version_name],
            capture_output=True, text=True, check=False
        )

        if not branch_result.stdout and not tag_result.stdout:
            raise PackageDoesNotExist(f'Neither branch nor tag "{version_name}" exists on "{repo_url}"')
