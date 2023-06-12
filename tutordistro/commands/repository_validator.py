import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.repository_validator.application.dpkg_url_validator import DPKGUrlValidator
from tutordistro.distro.repository_validator.application.extra_pip_requirements_url_validator import \
    ExtraPipRequirementsUrlValidator
from tutordistro.distro.repository_validator.infrastructure.git_package_repository import GitPackageRepository
from tutordistro.utils.packages import (
    get_public_distro_packages
)


@click.command(name="repository-validator", help="Repository validator")
def repository_validator() -> None:    # pylint: disable=missing-function-docstring
    directory = subprocess.check_output("tutor config printroot", shell=True).\
        decode("utf-8").strip()
    config = tutor_config.load(directory)

    public_packages = get_public_distro_packages(config)

    repository = GitPackageRepository()
    dpkg_controller = DPKGUrlValidator(repository=repository)

    # Check github repos that end with 'DPKG'

    for package in public_packages.values():
        try:
            dpkg_controller(
                name=package["name"],
                version=package["version"],
                domain=package["domain"],
                extra={
                    "repo": package["repo"],
                    "protocol": package["protocol"],
                    "path": package["path"]
                }
            )
        except Exception as error: # pylint: disable=broad-except
            click.echo(error)

    # Check the openedx_extra_pip_requirements repos
    openedx_extra_pip_requirements = config.get('OPENEDX_EXTRA_PIP_REQUIREMENTS', [])

    epr_controller = ExtraPipRequirementsUrlValidator(repository=repository)

    for git_url in openedx_extra_pip_requirements:
        try:
            epr_controller(url=git_url)
        except Exception as error: # pylint: disable=broad-except
            click.echo(error)
                