"""Command Manager"""

import abc
from abc import abstractmethod


class CommandManager(metaclass=abc.ABCMeta):
    """Command Manager"""

    @abstractmethod
    def run_command(self, command: str):
        """Run a command."""
