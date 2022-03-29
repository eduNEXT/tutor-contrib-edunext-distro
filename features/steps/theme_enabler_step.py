import json

from behave import given

from tutordistro.distro.domain.theme_settings import ThemeSettings


@given("There are {settings}")
def step_impl(context, settings):
    settings = json.loads(settings)
    ThemeSettings(
        settings=settings,
    )
