Feature: Theme Enabler
    @fixture.behave.tutor_root
    Scenario: Cloning repo
        Given There is a tutor root
        And There is a config.yml file
        When I write the command tutor distro enable-themes without confirm
        Given There is a DISTRO_THEMES and DISTRO_THEMES_ROOT in config.yml
        Then Themes will be cloned into theme folder

    @fixture.behave.tutor_root
    Scenario: Cloning repo with dir exists
        Given There is a tutor root
        And There is a config.yml file
        Given There is a DISTRO_THEMES and DISTRO_THEMES_ROOT in config.yml
        And Already exist theme folder
        When I write the command tutor distro enable-themes and press no
        Then The folder wasn't modified
