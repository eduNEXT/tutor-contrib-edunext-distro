"""
Tutor distro plugin tests
"""

from tutordistro.__about__ import __version__


def test_version():
    """
    Tutor distro plugin tests version
    """
    assert __version__ == '3.0.0-rc1'
