
import os
import subprocess

from behave import given, when, then    # pylint: disable=no-name-in-module
from click.testing import CliRunner
from tutor import config as tutor_config

from tutordistro.commands.enable_themes import enable_themes


@given("There is a tutor root")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    os.environ['TUTOR_ROOT'] = context.scenario.tutor_root
    output = subprocess.check_output("tutor config printroot", shell=True)
    output_formated = output.decode("utf-8").strip()
    context.scenario.tutor_root = output_formated
    assert os.path.exists(output_formated)


@given("There is a config.yml file")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    subprocess.call("tutor plugins enable distro", shell=True)
    subprocess.call("tutor config save", shell=True)
    config = tutor_config.load(context.scenario.tutor_root)
    context.scenario.config = config
    assert os.path.exists(f"{context.scenario.tutor_root}/config.yml")


@given("Already exist theme folder")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    name = context.scenario.config["DISTRO_THEMES"][0]["name"]
    path = f"{context.scenario.tutor_root}/env/build\
    {context.scenario.config['DISTRO_THEMES_ROOT']}/{name}"
    os.makedirs(path)
    assert os.path.exists(path)


@when("I write the command tutor distro enable-themes without confirm")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(enable_themes, obj=context)
    assert result.exit_code == 0


@when("I write the command tutor distro enable-themes and press no")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(enable_themes, obj=context, input="n")
    print(result)
    assert result.exit_code == 0


@then("Themes will be cloned into theme folder")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    distro_theme_root = context.scenario.config["DISTRO_THEMES_ROOT"]
    themes = context.scenario.config["DISTRO_THEMES"]
    for theme in themes:
        path = f"{context.scenario.tutor_root}/env/build{distro_theme_root}/{theme['name']}"
        assert os.path.exists(path)


@then("The folder wasn't modified")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    name = context.scenario.config["DISTRO_THEMES"][0]["name"]
    path = f"{context.scenario.tutor_root}/env/build\
    {context.scenario.config['DISTRO_THEMES_ROOT']}/{name}"
    assert len(os.listdir(path)) == 0
