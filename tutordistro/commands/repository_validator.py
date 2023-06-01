import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.repository_validator.application.git_url_edx_platform_repository_validator import GitURLEdxPlatformRepositoryValidator
from tutordistro.distro.repository_validator.application.git_url_openedx_extra_pip_requirements_validator import GitURLOpenedxExtraPipRequirementsValidator
from tutordistro.distro.repository_validator.application.git_url_validator import GitURLValidator


def get_distro_packages(settings) -> list:
    distro_packages = {key: val for key,
                       val in settings.items() if key.endswith("_DPKG") and val != 'None'}
    return distro_packages


def get_public_distro_packages(settings) -> list:
    distro_packages = get_distro_packages(settings)
    public_packages = {key: val for key,
                        val in distro_packages.items() if not val["private"]}
    return public_packages


@click.command(name="repository-validator", help="Repository validator")
def repository_validator() -> None:    # pylint: disable=missing-function-docstring
    directory = subprocess.check_output("tutor config printroot", shell=True).\
        decode("utf-8").strip()
    config = tutor_config.load(directory)

    public_packages = get_public_distro_packages(config)

    for package in public_packages.values():
        try:
            validator = GitURLValidator(package)
            validator.validate()
            
        except Exception as error: # pylint: disable=broad-except
            click.echo(error)
    
    edx_platform_repository_validate = GitURLEdxPlatformRepositoryValidator(config.get('EDX_PLATFORM_REPOSITORY', ""), config.get('EDX_PLATFORM_VERSION', ""))
    try:
        edx_platform_repository_validate.validate()
    except Exception as error: # pylint: disable=broad-except
        click.echo(error)

    openedx_extra_pip_requirements = config.get('OPENEDX_EXTRA_PIP_REQUIREMENTS', [])

    for git_url in openedx_extra_pip_requirements:
        openedx_extra_pip_requirements_validate = GitURLOpenedxExtraPipRequirementsValidator(git_url)
        try:
            openedx_extra_pip_requirements_validate.validate()
        except Exception as error: # pylint: disable=broad-except
            click.echo(error)