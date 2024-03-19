"""
Distro run extra commands command.
"""

import subprocess

import click
from tutor import config as tutor_config

from tutordistro.distro.extra_commands.application.commands_runner import CommandsRunner
from tutordistro.distro.extra_commands.infrastructure.tutor_commands import (
    TutorCommandManager,
)


@click.command(name="run-extra-commands", help="Run distro extra commands")
def run_extra_commands():
    """
    This command runs the distro extra commands
    """
    directory = (
        subprocess.check_output("tutor config printroot", shell=True)
        .decode("utf-8")
        .strip()
    )
    config = tutor_config.load(directory)

    tutor_commands_manager = TutorCommandManager()
    run_tutor_command = CommandsRunner(commands_manager=tutor_commands_manager)

    if config.get("DISTRO_EXTRA_COMMANDS"):
        for command in config["DISTRO_EXTRA_COMMANDS"]:
            run_tutor_command(command=command, tutor_root=directory)
