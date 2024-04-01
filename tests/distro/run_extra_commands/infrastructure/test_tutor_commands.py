"""
Test tutor commands functions.
"""

from tutordistro.distro.extra_commands.infrastructure.tutor_commands import TutorCommandManager


class TestTutorCommandManager(TutorCommandManager):
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

        self.commands_ran += 1
