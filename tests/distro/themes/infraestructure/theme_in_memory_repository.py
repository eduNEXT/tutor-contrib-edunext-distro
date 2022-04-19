from tutordistro.distro.themes.domain.theme_repository import ThemeRepository
from tutordistro.distro.packages.share.domain.clone_exception import CloneException
from tutordistro.distro.themes.domain.theme_settings import ThemeSettings


class ThemeInMemoryRepository(ThemeRepository):

    DIRS = []

    def __init__(self, theme_settings: ThemeSettings, repo_exists: bool):
        self.theme_settings = theme_settings
        self.repo_exists = repo_exists

    def clone(self) -> None:
        if not self.repo_exists:
            raise CloneException(
                """
                Finish not success.
                There are a trouble to enable themes.
                """
            )

        full_theme_path = f"Cloned from {self.theme_settings.name} to {self.theme_settings.get_full_directory}"  # pylint: disable=line-too-long
        self.DIRS.append(full_theme_path)

    def check_directory(self) -> None:
        for elem in self.DIRS:
            if self.theme_settings.get_full_directory in elem:
                self.DIRS.remove(elem)
