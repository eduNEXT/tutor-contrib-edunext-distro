Feature: Run extra commands
    @fixture.behave.tutor_root
    Scenario: Execute the extra commands from config.yml properly
        Given There is a tutor root
        And There is a config.yml file
        And There are valid commands defined
        When I write the command tutor distro run-extra-commands and commands will be properly executed

    @fixture.behave.tutor_root
    Scenario: Execute commands that are not valid
        Given There is a tutor root
        And There is a config.yml file
        And There are invalid commands defined
        When I write the command tutor distro run-extra-commands and commands execution will fail
