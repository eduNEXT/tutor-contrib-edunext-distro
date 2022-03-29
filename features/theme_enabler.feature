Feature: Theme Enabler
    @fixture.behave.tutor_root
    @fixture.behave.tutor_config
    Scenario Outline: Cloning repo
        Given There are <theme_settings>
        And There is an existent repository
        And There is a theme folder created
        When I write the command tutor distro enable-themes
        Then Themes will be cloned into theme folder

    Examples:
        | theme_settings |
        |{"version": "123", "repo": "ednx_saas", "branch": "master", "protocol": "https", "domain": "domain_test", "path":"ednx_saas"}|
