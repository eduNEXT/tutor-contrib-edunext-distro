"""
Theme in memory repository infrastructure.
"""

from tutordistro.distro.packages.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeInMemoryRepository(ThemeRepository):  # pylint: disable=too-few-public-methods
    """
    In-memory theme repository.

    This class represents an in-memory repository for themes.
    It provides the functionality to clone themes and stores
    the information about the cloned themes in memory.
    """

    DIRS = []

    def __init__(self, repo_exists: bool) -> None:
        self.repo_exists = repo_exists

    def clone(self, theme_settings: ThemeSettings) -> None:
        """
        Clone the theme repository.

        This method clones the theme repository based on the provided theme settings.

        Args:
            theme_settings (ThemeSettings): Theme settings.
        """
        if not self.repo_exists:
            raise CloneException(
                """
                Finish not success.
                There are a trouble to enable themes.
                """
            )

        full_theme_path = (
            f"Cloned from {theme_settings.name} to "
            f"{theme_settings.get_full_directory}"
        )
        self.DIRS.append(full_theme_path)
