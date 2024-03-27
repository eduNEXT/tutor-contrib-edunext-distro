import os

import subprocess

from behave import given, when, then    # pylint: disable=no-name-in-module
from click.testing import CliRunner
from tutor import config as tutor_config

from tutordistro.commands.run_extra_commands import run_extra_commands


@given("There are valid commands defined")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    extra_commands = [
        "tutor plugins update",
        "tutor plugins install forum",
        "tutor plugins enable forum"
    ]

    config = context.scenario.config
    config.update({
        "DISTRO_EXTRA_COMMANDS": extra_commands
    })

    tutor_config.save_config_file(context.scenario.tutor_root, config)
    config = tutor_config.load(context.scenario.tutor_root)
    context.scenario.config = config
    context.scenario.extra_commands = "DISTRO_EXTRA_COMMANDS"

    assert "DISTRO_EXTRA_COMMANDS" in config


@given("There are invalid commands defined")
def step_impl(context):  # pylint: disable=function-redefined,missing-function-docstring
    extra_commands = [
        "pip install application"
    ]

    config = context.scenario.config
    config.update({
        "DISTRO_EXTRA_COMMANDS": extra_commands
    })

    tutor_config.save_config_file(context.scenario.tutor_root, config)
    config = tutor_config.load(context.scenario.tutor_root)
    context.scenario.config = config
    context.scenario.extra_commands = "DISTRO_EXTRA_COMMANDS"

    assert "DISTRO_EXTRA_COMMANDS" in config


@when("I write the command tutor distro run-extra-commands and commands will be properly executed")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(run_extra_commands, obj=context)
    assert result.exit_code == 0


@when("I write the command tutor distro run-extra-commands and commands execution will fail")
def step_impl(context): # pylint: disable=function-redefined,missing-function-docstring
    runner = CliRunner()
    result = runner.invoke(run_extra_commands, obj=context)
    assert result.exit_code != 0

