"""
Test run commands application.
"""

import pytest

from tests.distro.run_extra_commands.infrastructure.test_tutor_commands import TestTutorCommandManager
from tutordistro.distro.extra_commands.application.commands_runner import CommandsRunner
from tutordistro.distro.share.domain.command_error import CommandError


def test_valid_tutor_command():
    """
    Test running valid commands.

    This test verifies that are executed all the extra commands successfully.
    """
    # Given
    tutor_commands_manager = TestTutorCommandManager()
    run_tutor_command = CommandsRunner(commands_manager=tutor_commands_manager)

    valid_tutor_commands = [
        "command with word tutor 1",
        "command with word tutor 2",
        "command with word tutor 3",
    ]

    # When
    for command in valid_tutor_commands:
        run_tutor_command(command=command)

    assert tutor_commands_manager.commands_ran == len(valid_tutor_commands)


def test_invalid_tutor_command():
    """
    Test running invalid commands.

    This test verifies that the execution fails when is
    intended to execute invalid extra commands.
    """
    # Given
    tutor_commands_manager = TestTutorCommandManager()
    run_tutor_command = CommandsRunner(commands_manager=tutor_commands_manager)

    invalid_tutor_command = "pip command 1"

    # When
    with pytest.raises(CommandError) as command_error:
        run_tutor_command(command=invalid_tutor_command)

    assert command_error.type is CommandError
    assert "is not a valid Tutor command" in command_error.value.args[0]


def test_misspelled_tutor_command():
    """
    Test running misspelled Tutor commands.

    This test verifies that is warned the user of trying to execute
    a misspelled Tutor command.
    """
    # Given
    tutor_commands_manager = TestTutorCommandManager()
    run_tutor_command = CommandsRunner(commands_manager=tutor_commands_manager)

    invalid_tutor_command = "totur command bad written"

    # When
    with pytest.raises(CommandError) as command_error:
        run_tutor_command(command=invalid_tutor_command)

    assert command_error.type is CommandError
    assert "you have a typo" in command_error.value.args[0]
