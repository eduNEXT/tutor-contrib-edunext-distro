import pytest
from tests.distro.infraestructure.distro_in_memory_repository import (
    DistroInMemoryRepository,
)
from tutordistro.distro.domain.git_clone_exception import GitCloneException
from tutordistro.distro.domain.theme_settings import ThemeSettings


def test_clone_when_repo_exists():
    theme_settings = ThemeSettings(
        theme_settings={
            "version": "123",
            "repo": "ednx_saas",
            "branch": "master",
            "protocol": "https",
            "domain": "domain_test",
            "path": "ednx_saas",
        },
        tutor_root="/path/to/tutor",
        tutor_config={"DISTRO_THEMES_ROOT": "distro_themes"},
    )
    repo_exists = True
    repository = DistroInMemoryRepository(
        theme_settings=theme_settings, repo_exists=repo_exists
    )
    repository.clone()
    full_path_theme = f"Cloned from https://domain_test/ednx_saas/ednx_saas to /path/to/tutor/env/build/distro_themes"

    assert full_path_theme in repository.DIRS

def test_clon_with_repo_does_not_exists():
    theme_settings = ThemeSettings(
        theme_settings={
            "version": "123",
            "repo": "ednx_saas",
            "branch": "master",
            "protocol": "https",
            "domain": "domain_test",
            "path": "ednx_saas",
        },
        tutor_root="/path/to/tutor",
        tutor_config={"DISTRO_THEMES_ROOT": "distro_themes"},
    )
    repo_exists = False
    repository = DistroInMemoryRepository(
        theme_settings=theme_settings, repo_exists=repo_exists
    )
    with pytest.raises(GitCloneException) as git_error:
        repository.clone()
    assert git_error.type is GitCloneException

def test_clone_when_directory_exists():
    theme_settings = ThemeSettings(
        theme_settings={
            "version": "123",
            "repo": "ednx_saas",
            "branch": "master",
            "protocol": "https",
            "domain": "domain_test",
            "path": "ednx_saas",
        },
        tutor_root="/path/to/tutor",
        tutor_config={"DISTRO_THEMES_ROOT": "distro_themes"},
    )
    repo_exists = True
    repository = DistroInMemoryRepository(
        theme_settings=theme_settings, repo_exists=repo_exists
    )
    assert len(repository.DIRS) != 0
    repository.check_directory()
    assert len(repository.DIRS) == 0
    repository.clone()
    assert len(repository.DIRS) != 0
