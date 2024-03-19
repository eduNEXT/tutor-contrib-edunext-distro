"""
Distro theme funtions.
"""

import os
import shutil
import subprocess

import click

from tutordistro.distro.extra_commands.domain.command_manager import CommandManager
from tutordistro.distro.share.domain.command_error import CommandError


class TutorCommandManager(CommandManager):
    """
    Executes a Tutor extra command.

    This class provides functionality to execute an extra Tutor command.

    Args:
        CommandManager (class): Base command manager class.
    """

    def run_command(self, command: str, tutor_root: str):
        """
        Run an extra command.

        This method runs the extra command provided.

        Args:
            command (str): Tutor command.
            tutor_root (str): Tutor path where to execute the command.
        """
        """Run a command."""
        try:
            if "tutor" not in command.lower():
                raise CommandError(f'Command {command} is not a valid Tutor command')

            subprocess.run(f'source {tutor_root}/.tvm/bin/activate &&'
                           f'{command} && tvmoff',
                           shell=True, check=False,
                           executable='/bin/bash')
        except subprocess.SubprocessError as error:
            raise CommandError(f'Error running command {command}') from error
