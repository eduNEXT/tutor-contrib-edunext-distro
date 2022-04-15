import pytest
from tests.distro.themes.infraestructure.theme_in_memory_repository import (
    ThemeInMemoryRepository,
)
from tutordistro.distro.packages.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


def test_clone_when_repo_exists():
    theme_settings = ThemeSettings(
        settings={
            "version": "123",
            "repo": "ednx_saas",
            "name": "ednx_saas",
            "branch": "master",
            "protocol": "https",
            "domain": "domain_test",
            "path": "ednx_saas",
        },
        tutor_root="/path/to/tutor",
        tutor_config={"DISTRO_THEMES_ROOT": "/openedx/themes"},
    )
    repo_exists = True
    repository = ThemeInMemoryRepository(
        theme_settings=theme_settings, repo_exists=repo_exists
    )
    repository.clone()
    full_path_theme = f"Cloned from ednx_saas to /path/to/tutor/env/build/openedx/themes/ednx_saas"

    print("FULL_PATH", full_path_theme)
    print("REPOSITORY DISRS:", repository.DIRS)

    assert full_path_theme in repository.DIRS

def test_clon_with_repo_does_not_exists():
    theme_settings = ThemeSettings(
        settings={
            "version": "123",
            "repo": "ednx_saas",
            "name": "ednx_saas",
            "branch": "master",
            "protocol": "https",
            "domain": "domain_test",
            "path": "ednx_saas",
        },
        tutor_root="/path/to/tutor",
        tutor_config={"DISTRO_THEMES_ROOT": "/openedx/themes"},
    )
    repo_exists = False
    repository = ThemeInMemoryRepository(
        theme_settings=theme_settings, repo_exists=repo_exists
    )
    with pytest.raises(CloneException) as git_error:
        repository.clone()
    assert git_error.type is CloneException

def test_clone_when_directory_exists():
    theme_settings = ThemeSettings(
        settings={
            "version": "123",
            "repo": "ednx_saas",
            "name": "ednx_saas",
            "branch": "master",
            "protocol": "https",
            "domain": "domain_test",
            "path": "ednx_saas",
        },
        tutor_root="/path/to/tutor",
        tutor_config={"DISTRO_THEMES_ROOT": "/openedx/themes"},
    )
    repo_exists = True
    repository = ThemeInMemoryRepository(
        theme_settings=theme_settings, repo_exists=repo_exists
    )
    assert len(repository.DIRS) != 0
    repository.check_directory()
    assert len(repository.DIRS) == 0
    repository.clone()
    assert len(repository.DIRS) != 0
