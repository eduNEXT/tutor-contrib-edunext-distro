"""
Distro command runner.
"""
from tutordistro.distro.extra_commands.domain.command_manager import CommandManager


class CommandsRunner:
    """
    Command runner.

    This class is responsible of executing extra commands by invoking the run_command method
    on a commands manager.

    Attributes:
        commands_manager (ThemeRepository): The command manager to use for executing the extra command.
    """

    def __init__(self, commands_manager: CommandManager):
        self.commands_manager = commands_manager

    def __call__(self, command: str, tutor_root: str):
        """
        Run the provided command.

        This method runs the provided command by invoking the run_command method
        from the given command manager

        Args:
            command (str): Command to execute.
        """

        return self.commands_manager.run_command(command=command, tutor_root=tutor_root)
