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
    plugin_directory = directory + "/tutor-contrib-edunext-distro/tutordistro/plugin.py"
    print('hi')
    print(plugin_directory)
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
                extra={  # pylint:disable=duplicate-code
                    "repo": package["repo"],
                    "protocol": package["protocol"],
                    "path": package["path"]
                },
                path=requirements_directory
            )
            definer(name=package["name"],
                    file_path=f"{requirements_directory}private.txt")

            # Run tutor mounts add command for the package
            subprocess.check_output(f"tutor mounts add {requirements_directory}{package['name']}", shell=True)
            hook = f'hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", "{package["name"]}"))'

            hook_writer(file_path=plugin_directory, hook_to_append=hook)
            subprocess.check_output("tutor config save", shell=True)
        except Exception as error:  # pylint: disable=broad-exception-caught
            click.echo(error)


def hook_writer(file_path, hook_to_append):
    """
    Function to write the corresponding hooks depending on the private packages.
    """

    with open(file_path, 'a+', encoding='utf-8') as my_file:  # Open file in append and read mode

        my_file.seek(0)  # Move the cursor to the beginning of the file
        existing_lines = my_file.readlines()
        package_name = hook_to_append.split('"')[3]  # Extract package name from hook_to_append

        # Check if package name already exists in the file
        if any(package_name in line for line in existing_lines):
            print(f"Package '{package_name}' already present in the file.")
        else:
            my_file.write(hook_to_append + "\n")
