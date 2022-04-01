"""
Tutor data manager behave hooks
"""

from behave.fixture import use_fixture_by_tag
from behave import use_fixture

from features.fixtures.tutor_root import (
    behave_tutor_root,
    behave_tutor_clean,
)

fixture_registry = {
    "fixture.behave.tutor_root": behave_tutor_root,
}


def before_scenario(context, scenario):
    """
    Exec this code before each scenario
    """
    for tag in scenario.tags:
        use_fixture_by_tag(tag, context, fixture_registry)


def after_scenario(context, scenario):
    """
    Exec this code after each scenario
    """
    if "fixture.behave.tutor_root" in scenario.tags:
        use_fixture(behave_tutor_clean, context)
