"""
Tutor data manager behave fixtures
"""

import os
import shutil

from datetime import datetime
from pathlib import Path

from behave import fixture


@fixture(name="fixture.behave.tutor_root")
def behave_tutor_root(ctx):
    """
    Create a folder to use as tutor root
    """
    current_scenario = ctx.scenario
    if current_scenario:
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        basedir = os.path.dirname(os.path.dirname(__file__))
        tutor_root = os.path.join(basedir, f"tutor_test_{timestamp}")
        if os.path.exists(tutor_root):
            os.rmdir(tutor_root)
        os.mkdir(tutor_root)
        os.makedirs(f"{tutor_root}/env/build/openedx/themes")
        current_scenario.tutor_root = tutor_root


@fixture(name="fixture.behave.tutor_clean")
def behave_tutor_clean(ctx):
    """
    Remove tutor root folders used on the scenarios
    """
    current_scenario = ctx.scenario
    if current_scenario.tutor_root:
        shutil.rmtree(current_scenario.tutor_root)
