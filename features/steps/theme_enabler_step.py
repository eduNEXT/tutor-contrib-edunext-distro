import json
import os
import subprocess

from behave import given, when
from click.testing import CliRunner
from tutor.commands.context import Context

from tutordistro.distro.domain.theme_settings import ThemeSettings
from tutordistro.commands.enable_themes import enable_themes


@given("There is a tutor root")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    os.environ['TUTOR_ROOT'] = context.scenario.tutor_root
    output = subprocess.check_output("tutor config printroot", shell=True)
    output_formated = output.decode("utf-8").strip()

    subprocess.call("tutor plugins enable distro", shell=True)
    subprocess.call("tutor config save", shell=True)
    assert os.path.exists(output_formated)


@given("There is theme setting valid {theme_settings}")
def step_impl(context, theme_settings): # pylint: disable=function-redefined,missing-function-docstring
    pass


@given("There is an existent repository in git")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    pass


@when("I write the command tutor distro enable-themes")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(enable_themes, obj=context)
    print(result)
    assert result.exit_code == 0

