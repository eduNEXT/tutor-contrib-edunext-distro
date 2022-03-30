Feature: Theme Enabler
    @fixture.behave.tutor_root
    Scenario Outline: Cloning repo
        Given There is a tutor root
        And There is theme setting valid <theme_settings>
        When I write the command tutor distro enable-themes
        Then Themes will be cloned into theme folder

    Examples:
        | theme_settings |
        |{"version": "123", "repo": "ednx_saas", "name": "ednx_saas", "branch": "master", "protocol": "https", "domain": "domain_test", "path":"ednx_saas"}|
