"""
Test cloner theme enabler application.
"""

import pytest

from tests.distro.themes.infraestructure.theme_in_memory_repository import ThemeInMemoryRepository
from tutordistro.distro.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.application.theme_enabler import ThemeEnabler


def test_clone_when_repo_exists():
    """
    Test cloning when the repository exists.

    This test verifies that the theme is cloned successfully when the repository exists.
    """
    # Given
    repo_exists = True
    repository = ThemeInMemoryRepository(repo_exists=repo_exists)
    enabler = ThemeEnabler(repository=repository)
    settings = {
        "version": "123",
        "repo": "ednx_saas",
        "name": "ednx_saas",
        "branch": "master",
        "protocol": "https",
        "domain": "domain_test",
        "path": "ednx_saas",
    }
    tutor_root = "/path/to/tutor"
    tutor_config = {"DISTRO_THEMES_ROOT": "/openedx/themes"}

    # When
    enabler(settings=settings, tutor_root=tutor_root, tutor_config=tutor_config)

    full_path_theme = (
        f"Cloned from ednx_saas to {tutor_root}/env/build"
        f"{tutor_config['DISTRO_THEMES_ROOT']}/"
        f"{settings['name']}"
    )
    assert full_path_theme in repository.DIRS


def test_clon_with_repo_does_not_exists():
    """
    Test cloning when the repository does not exist.

    This test verifies that a CloneException is raised when trying
    to clone a theme from a non-existing repository.
    """
    # Given
    repo_exists = False
    repository = ThemeInMemoryRepository(repo_exists=repo_exists)
    enabler = ThemeEnabler(repository=repository)
    settings = {
        "version": "123",
        "repo": "ednx_saas",
        "name": "ednx_saas",
        "branch": "master",
        "protocol": "https",
        "domain": "domain_test",
        "path": "ednx_saas",
    }
    tutor_root = "/path/to/tutor"
    tutor_config = {"DISTRO_THEMES_ROOT": "/openedx/themes"}

    with pytest.raises(CloneException) as git_error:
        # When
        enabler(settings=settings, tutor_root=tutor_root, tutor_config=tutor_config)
    # Then
    assert git_error.type is CloneException
