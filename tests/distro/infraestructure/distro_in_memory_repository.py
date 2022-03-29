from tutordistro.distro.domain.distro_repository import DistroRepository
from tutordistro.distro.domain.git_clone_exception import GitCloneException
from tutordistro.distro.domain.theme_settings import ThemeSettings


class DistroInMemoryRepository(DistroRepository):
    """ """

    DIRS = []

    def __init__(self, theme_settings: ThemeSettings, repo_exists: bool):
        self.theme_settings = theme_settings
        self.repo_exists = repo_exists

    def clone(self):
        if not self.repo_exists:
            raise GitCloneException(
                f"""
                Finish not success.
                There are a trouble to enable themes.
                """
            )
        else:
            full_theme_path = f"Cloned from {self.theme_settings.repo} to {self.theme_settings.get_full_directory}"
            self.DIRS.append(full_theme_path)

    def check_directory(self) -> None:
        for elem in self.DIRS:
            if self.theme_settings.get_full_directory in elem:
                self.DIRS.remove(elem)


    def create_directory(self) -> None:
        return super().create_directory()
