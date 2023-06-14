"""
Tutor distro plugin tests
"""

import re

from tutordistro.__about__ import __version__


def test_version():
    """
    Tutor distro plugin tests version
    """
    version = get_current_version()
    assert __version__ == version


def get_current_version():
    """
    Get the current version from 'setup.cfg'
    """
    with open('setup.cfg', 'r', encoding='utf-8') as f_setup:
        file = f_setup.read()
    pattern_version = re.escape("current_version = ") + r"\d+\.\d+\.\d+"
    version = re.findall(pattern_version, file)
    current_version = version[0].split("=")[1].split()

    return current_version[0]
