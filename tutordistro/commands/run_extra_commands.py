"""
Distro run extra commands command.
"""

import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.extra_commands.application.commands_runner import CommandsRunner
from tutordistro.distro.extra_commands.infrastructure.tutor_commands import TutorCommandManager


@click.command(name="run-extra-commands", help="Run tutor commands")
def run_extra_commands():
    """
    This command runs tutor commands defined in DISTRO_EXTRA_COMMANDS
    """
    directory = (
        subprocess.check_output("tutor config printroot", shell=True)
        .decode("utf-8")
        .strip()
    )
    config = tutor_config.load(directory)
    distro_extra_commands = config.get("DISTRO_EXTRA_COMMANDS", None)

    tutor_commands_manager = TutorCommandManager()
    run_tutor_command = CommandsRunner(commands_manager=tutor_commands_manager, commands=distro_extra_commands)

    if distro_extra_commands:
        for command in distro_extra_commands:
            run_tutor_command(command=command)
