"""
Distro tutor command functions.
"""

import subprocess
# Was necessary to use this for compatibility with Python 3.8
from typing import List

from tutordistro.distro.extra_commands.domain.command_manager import CommandManager
from tutordistro.distro.share.domain.command_error import CommandError
from tutordistro.utils.common import find_tutor_misspelled, split_string
from tutordistro.utils.constants import COMMAND_CHAINING_OPERATORS


class TutorCommandManager(CommandManager):
    """
    Executes a Tutor extra command.

    This class provides functionality to execute an extra Tutor command.

    Args:
        CommandManager (class): Base command manager class.
    """

    def validate_commands(self, commands: List[str]):
        """
        Takes all the extra commands sent through config.yml and verifies that
        all the commands are correct before executing them

        Args:
            commands (list[str] | None): The commands sent through DISTRO_EXTRA_COMMANDS in config.yml
        """
        splitted_commands = [
            split_string(command, COMMAND_CHAINING_OPERATORS) for command in commands
        ]
        flat_commands_array = sum(splitted_commands, [])

        invalid_commands = []
        misspelled_commands = []
        for command in flat_commands_array:
            if "tutor" not in command.lower():
                if find_tutor_misspelled(command):
                    misspelled_commands.append(command)
                else:
                    invalid_commands.append(command)

        if invalid_commands or misspelled_commands:
            raise CommandError(
                f"""
                Error: Were found some issues with the commands:

                {'=> Invalid commands: ' if invalid_commands else ""}
                {', '.join(invalid_commands)}

                {'=> Misspelled commands: ' if misspelled_commands else ""}
                {', '.join(misspelled_commands)}

                Take a look of the official Tutor commands: https://docs.tutor.edly.io/reference/cli/index.html
                """
            )

    def run_command(self, command: str):
        """
        Run an extra command.

        This method runs the extra command provided.

        Args:
            command (str): Tutor command.
        """
        try:
            process = subprocess.run(
                command,
                shell=True,
                check=True,
                capture_output=True,
                executable="/bin/bash",
            )
            # This print is left on purpose to show the command output
            print(process.stdout.decode())

        except subprocess.CalledProcessError as error:
            raise CommandError(
                f"Error running command '{error.cmd}':\n{error.stderr.decode()}"
            ) from error
