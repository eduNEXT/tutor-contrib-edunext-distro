"""
Distro tutor command functions.
"""

import re
import subprocess

from tutordistro.distro.extra_commands.domain.command_manager import CommandManager
from tutordistro.distro.share.domain.command_error import CommandError
from tutordistro.utils.constants import COMMAND_CHAINING_OPERATORS, create_regex_from_array, find_tutor_misspelled


class TutorCommandManager(CommandManager):
    """
    Executes a Tutor extra command.

    This class provides functionality to execute an extra Tutor command.

    Args:
        CommandManager (class): Base command manager class.
    """
    def split_command(self, command: str):
        """
        Takes a command that is wanted to be split according to some
        bash command chaining operators

        Args:
            command (str): Command with command chaining operator

        Return:
            The command split into an array
        """
        return re.split(create_regex_from_array(COMMAND_CHAINING_OPERATORS), command)

    def validate_commands(self, commands: list[str] | None):
        """
        Takes all the extra commands sent through config.yml and verifies that
        all the commands are correct before executing them

        Args:
            commands (list[str] | None): The commands sent through DISTRO_EXTRA_COMMANDS in config.yml
        """
        if not commands:
            raise CommandError(
                "No commands found in the DISTRO_EXTRA_COMMANDS attribute of the config.yml file."
            )

        splitted_commands = [self.split_command(command) for command in commands]
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
            with subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                executable="/bin/bash",
            ) as process:
                output, error = process.communicate()
                # If a command failed
                if process.returncode != 0:
                    raise CommandError(
                        f'Error running command "{command}".\n{error.decode()}'
                    )
                # This print is left on purpose to show the command output
                print(output.decode())

        except subprocess.SubprocessError as error:
            raise CommandError(f"Error running command {command}: {error}") from error
