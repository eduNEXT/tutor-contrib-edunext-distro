"""
Distro enable private packages command.
"""

import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.packages.application.package_cloner import PackageCloner
from tutordistro.distro.packages.application.private_package_definer import PrivatePackageDefiner
from tutordistro.distro.packages.infrastructure.package_git_repository import PackageGitRepository
from tutordistro.utils.packages import get_private_distro_packages


@click.command(name="enable-private-packages", help="Enable distro private packages")
def enable_private_packages():
    """
    Enable private packages command.

    This command enables distro private packages by cloning the packages and
    defining them as private.

    Raises:
        Exception: If an error occurs during the cloning or defining process.
    """
    directory = subprocess.check_output("tutor config printroot", shell=True).\
        decode("utf-8").strip()
    config = tutor_config.load(directory)

    repository = PackageGitRepository()
    cloner = PackageCloner(repository=repository)
    definer = PrivatePackageDefiner(repository=repository)

    private_packages = get_private_distro_packages(config)
    requirements_directory = f"{directory}/env/build/openedx/requirements/"
    for package in private_packages.values():
        try:
            cloner(
                name=package["name"],
                version=package["version"],
                domain=package["domain"],
                extra={
                    "repo": package["repo"],
                    "protocol": package["protocol"],
                    "path": package["path"]
                },
                path=requirements_directory
            )
            definer(name=package["name"],
                    file_path=f"{requirements_directory}private.txt")
        except Exception as error:  # pylint: disable=broad-exception-caught
            click.echo(error)
