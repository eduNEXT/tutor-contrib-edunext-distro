"""
Distro tutor commands functions.
"""

import os
import subprocess
import re

from tutordistro.distro.extra_commands.domain.command_manager import CommandManager
from tutordistro.distro.share.domain.command_error import CommandError


class TutorCommandManager(CommandManager):
    """
    Executes a Tutor extra command.

    This class provides functionality to execute an extra Tutor command.

    Args:
        CommandManager (class): Base command manager class.
    """

    def run_command(self, command: str):
        """
        Run an extra command.

        This method runs the extra command provided.

        Args:
            command (str): Tutor command.
            tutor_root (str): Tutor path where to execute the command.
        """
        try:
            is_tutor_bad_written = re.match(r'[tT](?:[oru]{3}|[oru]{2}[rR]|[oru]u?)', command)

            if "tutor" not in command.lower():
                if is_tutor_bad_written:
                    raise CommandError(f'Maybe you have a typo using the command "{command}"')
                else:
                    raise CommandError(f'Command "{command}" is not a valid Tutor command. Take the official Tutor commands into account https://docs.tutor.edly.io/reference/cli/index.html')
            
            process = subprocess.Popen(
                command,
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable='/bin/bash'
            )

            output, error = process.communicate()
            # If a command failed
            if process.returncode != 0:
                raise CommandError(f'Error running command "{command}".\n{output.decode()}\n{error.decode()}')

        except subprocess.SubprocessError as error:
            raise CommandError(f'Error running command {command}: {error}') from error
