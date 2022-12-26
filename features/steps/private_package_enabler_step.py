"""Theme enabler step definitions."""
import os

from behave import given, when, then    # pylint: disable=no-name-in-module
from click.testing import CliRunner
from tutor import config as tutor_config

from tutordistro.commands.enable_private_packages import \
    enable_private_packages, get_private_distro_packages


@when("I write the command tutor distro enable-private-packages")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(enable_private_packages, obj=context)
    assert result.exit_code == 0


@then("Packages will be cloned into requirements folder")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    distro_packages = get_private_distro_packages(context.scenario.config)
    for package in distro_packages.values():
        path = f"{context.scenario.tutor_root}/env/build/openedx/requirements/{package['name']}"
        assert os.path.exists(path)


@then("Packages will be present in the file private.txt")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    distro_packages = get_private_distro_packages(context.scenario.config)
    private_file = f"{context.scenario.tutor_root}/env/build/openedx/requirements/private.txt"
    with open(private_file, mode="r", encoding="utf-8") as private_requirements_file:
        for package in distro_packages.values():
            assert package["name"] in private_requirements_file.read()


@given("There is a private package")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    eox_test = {
        "index": "git",
        "name": "eox-test",
        "repo": "eox-tagging",
        "version": "v3.0.0",
        "domain": "github.com",
        "protocol": "ssh",
        "path": "eduNEXT",
        "variables": {
            "development": {},
            "production": {},
        },
        "private": True,
    }

    config = context.scenario.config
    config.update({
        "DISTRO_EOX_TEST_DPKG": eox_test
    })

    tutor_config.save_config_file(context.scenario.tutor_root, config)
    config = tutor_config.load(context.scenario.tutor_root)
    context.scenario.config = config
    context.scenario.private_package_key = "DISTRO_EOX_TEST_DPKG"

    assert "DISTRO_EOX_TEST_DPKG" in config


@given("Private package has already been cloned")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    private_package_key = context.scenario.private_package_key
    name = context.scenario.config[private_package_key]["name"]
    path = f"{context.scenario.tutor_root}/env/build/openedx/requirements/{name}"
    os.makedirs(path)
    assert os.path.exists(path) and len(os.listdir(path)) == 0


@when("I write the command tutor distro enable-private-packages and press yes")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(enable_private_packages, obj=context, input="y")
    assert result.exit_code == 0


@then("Packages will be cloned again into requirements folder")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    private_package_key = context.scenario.private_package_key
    name = context.scenario.config[private_package_key]["name"]
    path = f"{context.scenario.tutor_root}/env/build/openedx/requirements/{name}"
    assert len(os.listdir(path)) > 0
