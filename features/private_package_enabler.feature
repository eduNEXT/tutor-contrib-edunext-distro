Feature: Enable private packages
    @fixture.behave.tutor_root
    Scenario: Add private package to private requirements
        Given There is a tutor root
        And There is a config.yml file
        And There is a private package
        When I write the command tutor distro enable-private-packages
        Then Packages will be cloned into requirements folder

    @fixture.behave.tutor_root
    Scenario: Add private package when the package has already been cloned
        Given There is a tutor root
        And There is a config.yml file
        And There is a private package
        And Private package has already been cloned
        When I write the command tutor distro enable-private-packages and press yes
        Then Packages will be cloned again into requirements folder
