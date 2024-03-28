"""
Distro enable private packages command.
"""

import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.packages.application.package_cloner import PackageCloner
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

            # Run tutor mounts add command for the package
            subprocess.check_output(f"tutor mounts add {requirements_directory}{package['name']}", shell=True)
            hook = f'hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", "{package["name"]}"))'

            hook_writer(hook_to_append=hook)
            subprocess.check_output("tutor config save", shell=True)
        except Exception as error:  # pylint: disable=broad-exception-caught
            click.echo(error)


def get_distro_location():
    """
    Function to get the right distro path
    """

    try:
        result = subprocess.run(['pip', 'show', 'tutor-contrib-edunext-distro'],
                                capture_output=True, text=True, check=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Split the output into lines
            lines = result.stdout.splitlines()

            # Loop through each line to find the Location
            for line in lines:
                if line.startswith('Location:'):
                    # Extract the location path
                    location_path = line.split(':', 1)[1].strip() + "/tutordistro/plugin.py"
                    return location_path
    except subprocess.CalledProcessError as e:
        # Print error message if command failed
        print("Error running pip show distro:", e.stderr)

    # Return a default value if the location is not found or an error occurs
    return None


def hook_writer(hook_to_append):
    """
    Function to write the corresponding hooks depending on the private packages.
    """
    file_path = get_distro_location()
    with open(file_path, 'a+', encoding='utf-8') as my_file:  # Open file in append and read mode

        my_file.seek(0)  # Move the cursor to the beginning of the file
        existing_lines = my_file.readlines()
        package_name = hook_to_append.split('"')[3]  # Extract package name from hook_to_append

        # Check if package name already exists in the file
        if any(package_name in line for line in existing_lines):
            print(f"Package '{package_name}' already present in the file.")
        else:
            my_file.write(hook_to_append + "\n")
