"""Theme enabler step definitions."""
from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.packages.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeInMemoryRepository(ThemeRepository):  # pylint: disable=too-few-public-methods
    """Theme in memory repository."""
    DIRS = []

    def __init__(self, repo_exists: bool) -> None:
        self.repo_exists = repo_exists

    def clone(self, theme_settings: ThemeSettings) -> None:
        if not self.repo_exists:
            raise CloneException(
                """
                Finish not success.
                There are a trouble to enable themes.
                """
            )

        full_theme_path = f"Cloned from {theme_settings.name} to {theme_settings.get_full_directory}"  # pylint: disable=line-too-long
        self.DIRS.append(full_theme_path)
