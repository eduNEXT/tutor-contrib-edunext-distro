"""Test for clone theme enabler."""
import pytest
from tests.distro.themes.infraestructure.theme_in_memory_repository import (
    ThemeInMemoryRepository,
)
from tutordistro.distro.packages.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.application.theme_enabler import ThemeEnabler


def test_clone_when_repo_exists():
    """Test clone when repo exists."""
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

    full_path_theme = f"Cloned from ednx_saas to {tutor_root}/env/build{tutor_config['DISTRO_THEMES_ROOT']}/{settings['name']}"  # pylint: disable=line-too-long
    assert full_path_theme in repository.DIRS


def test_clon_with_repo_does_not_exists():
    """Test clone when repo does not exists."""
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
