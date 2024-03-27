"""
Test tutor commands functions.
"""

from tutordistro.distro.extra_commands.domain.command_manager import CommandManager
from tutordistro.distro.share.domain.command_error import CommandError
from tutordistro.utils.constants import find_tutor_misspelled


class TestTutorCommandManager(CommandManager):
    """
    Executes a Tutor command for testing.

    This class provides functionality to execute extra Tutor commands for testing.

    Args:
        CommandManager (class): Base command manager class.
    """
    commands_ran = 0

    def run_command(self, command: str):
        """
        This method runs an testing command.

        Args:
            command (str): Testing command.
        """
        is_tutor_misspelled = find_tutor_misspelled(command)

        if "tutor" not in command.lower():
            if is_tutor_misspelled:
                raise CommandError(
                    f'Maybe you have a typo using the command "{command}"'
                )
            raise CommandError(
                f'''
                    Command "{command}" is not a valid Tutor command.
                    Take the official Tutor commands into account
                    https://docs.tutor.edly.io/reference/cli/index.html
                '''
            )
        self.commands_ran += 1
