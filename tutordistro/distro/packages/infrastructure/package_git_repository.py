"""
Package git repository ingrastructure.
"""

import os
import shutil
import subprocess

import click

from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.share.domain.clone_exception import CloneException
from tutordistro.distro.share.domain.package import Package
from tutordistro.distro.share.domain.package_name import PackageName


class PackageGitRepository(PackageRepository):
    """
    Package Git repository infrastructure.

    This class provides functionality to clone and manage packages from a Git repository.
    """

    def set_as_private(self, name: PackageName, file_path: str) -> None:
        """
        Set a package as private.

        This method appends the package as a private requirement in the given requirements file.

        Args:
            name (PackageName): The name of the package.
            file_path (str): The file path of the requirements file.
        """
        already_exist = False

        if os.path.exists(file_path):
            with open(file_path, mode='r', encoding="utf-8") as private_requirements_file:
                if name in private_requirements_file.read():
                    already_exist = True

        if not already_exist:
            with open(file_path, mode='a+', encoding="utf-8") as private_requirements_file:
                private_requirements_file.write(f"\n-e ./{name}")

    def clone(self, package: Package, path: str) -> None:
        """
        Clone a package from the Git repository.

        This method clones the package from the specified Git repository.

        Args:
            package (Package): The package to be cloned.
            path (str): The destination path for cloning the package.
        """
        repo = None
        if "https" == package.extra["protocol"]:
            repo = (
                f"https://{package.domain}/"
                f"{package.extra['path']}/"
                f"{package.extra['repo']}"
            )
        elif "ssh" == package.extra["protocol"]:
            repo = (
                f"git@{package.domain}:"
                f"{package.extra['path']}/"
                f"{package.extra['repo']}.git"
            )

        package_folder = f"{path}{package.name}"

        if os.path.exists(f"{package_folder}"):
            if not click.confirm(f"Do you want to overwrite {package.name}? "):
                raise CloneException()
            shutil.rmtree(package_folder)

        subprocess.call(
            [
                "git",
                "clone",
                "-b",
                package.version,
                repo,
                f"{package_folder}",
            ]
        )
