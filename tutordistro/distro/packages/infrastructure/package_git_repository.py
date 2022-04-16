import os
import subprocess
import shutil
import click

from tutordistro.distro.packages.domain.package import Package
from tutordistro.distro.packages.domain.package_name import PackageName
from tutordistro.distro.packages.domain.package_repository import PackageRepository
from tutordistro.distro.packages.share.domain.clone_exception import CloneException


class PackageGitRepository(PackageRepository):
    def set_as_private(self, name: PackageName, file_path: str) -> None:
        already_exist = False

        if os.path.exists(file_path):
            with open(file_path, mode='r') as private_requirements_file:
                if name in private_requirements_file.read():
                    already_exist = True

        if not already_exist:
            with open(file_path, mode='a+') as private_requirements_file:
                private_requirements_file.write(f"\n-e ./{name}")

    def clone(self, package: Package, path: str) -> None:
        if "https" == package.extra["protocol"]:
            repo = f"https://{package.domain}/{package.extra['path']}/{package.extra['repo']}"  # pylint: disable=line-too-long
        elif "ssh" == package.extra["protocol"]:
            repo = f"git@{package.domain}:{package.extra['path']}/{package.extra['repo']}.git"  # pylint: disable=line-too-long

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
