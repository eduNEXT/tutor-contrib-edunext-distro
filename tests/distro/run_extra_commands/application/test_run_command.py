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
    valid_tutor_commands = [
        "command with word tutor 1",
        "command with word tutor 2",
        "command with word tutor 3",
    ]

    tutor_commands_manager = TestTutorCommandManager()
    run_tutor_command = CommandsRunner(commands_manager=tutor_commands_manager, commands=valid_tutor_commands)

    # When
    for command in valid_tutor_commands:
        run_tutor_command(command=command)

    assert tutor_commands_manager.commands_ran == len(valid_tutor_commands)


def test_invalid_or_misspelled_tutor_command():
    """
    Test running invalid commands.

    This test verifies that the execution fails when is
    intended to execute invalid extra commands.
    """
    # Given
    invalid_tutor_command = [
        "pip command 1",
        "tutor command && pip command 2",
        "tutor command & pip command 3",
        "tutor command || pip command 4",
        "tutor command | pip command 5",
        "tutor command ; pip command 6",
    ]

    with pytest.raises(CommandError) as command_error:
        tutor_commands_manager = TestTutorCommandManager()
        CommandsRunner(commands_manager=tutor_commands_manager, commands=invalid_tutor_command)

    assert command_error.type is CommandError

    splitted_commands = [tutor_commands_manager.split_command(command) for command in invalid_tutor_command]
    commands_word_by_word = " ".join(sum(splitted_commands, [])).split(" ")

    pip_commands_sent = commands_word_by_word.count("pip")
    pip_commands_found = command_error.value.args[0].split(" ").count("pip")

    assert pip_commands_sent == pip_commands_found


def test_misspelled_tutor_command():
    """
    Test running misspelled Tutor commands.

    This test verifies that is warned the user of trying to execute
    a misspelled Tutor command.
    """
    # Given
    misspelled_commands = [
        "totur command 1",
        "totur command 2",
        "totur command 3",
        "totur command 4",
        "totur command 5",
    ]

    with pytest.raises(CommandError) as command_error:
        tutor_commands_manager = TestTutorCommandManager()
        CommandsRunner(commands_manager=tutor_commands_manager, commands=misspelled_commands)

    assert command_error.type is CommandError

    splitted_commands = [tutor_commands_manager.split_command(command) for command in misspelled_commands]
    commands_word_by_word = " ".join(sum(splitted_commands, [])).split(" ")

    misspelled_commands_sent = commands_word_by_word.count("totur")
    misspelled_commands_found = command_error.value.args[0].split(" ").count("totur")

    assert misspelled_commands_sent == misspelled_commands_found
