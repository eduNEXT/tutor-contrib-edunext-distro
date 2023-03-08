"""
Tutor distro plugin tests
"""

from tutordistro.__about__ import __version__


def test_version():
    """
    Tutor distro plugin tests version
    """
    assert __version__ == '15.0.0'
