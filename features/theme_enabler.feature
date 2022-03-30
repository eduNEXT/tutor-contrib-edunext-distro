Feature: Theme Enabler
    @fixture.behave.tutor_root
    Scenario: Cloning repo
        Given There is a tutor root
        And There is a config.yml file
        When I write the command tutor distro enable-themes
        Then Themes will be cloned into theme folder
