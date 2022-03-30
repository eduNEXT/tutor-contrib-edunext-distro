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
    assert os.path.exists(output_formated)


@given("There is theme setting valid {theme_settings}")
def step_impl(context, theme_settings): # pylint: disable=function-redefined,missing-function-docstring
    theme_settings_dict = json.loads(theme_settings)
    theme_settings = ThemeSettings(
        settings=theme_settings_dict,
        tutor_root=context.scenario.tutor_root,
        tutor_config={"THEMES_ROOT": "/openedx/themes"}
    )
    context.scenario.theme_settings = theme_settings
    assert theme_settings

@given("There is an existent repository in git")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    theme_settings_dict = json.loads(theme_settings)
    theme_settings = ThemeSettings(
        settings=theme_settings_dict,
        tutor_root=context.scenario.tutor_root,
        tutor_config={"THEMES_ROOT": "/openedx/themes"}
    )
    context.scenario.theme_settings = theme_settings
    assert theme_settings

@when("I write the command tutor distro enable-themes")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(enable_themes, obj=context)
    print(result)
    assert result.exit_code == 0

