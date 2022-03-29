import os
import subprocess

from tutordistro.distro.domain.distro_repository import DistroRepository
from tutordistro.distro.domain.git_clone_exception import GitCloneException
from tutordistro.distro.domain.theme_settings import ThemeSettings


class DistroGitRepository(DistroRepository):
    def __init__(self, theme_settings: ThemeSettings):
        self.theme_settings = theme_settings

    def clone(self) -> None:
        result = subprocess.call(
            [
                "git",
                "clone",
                "-b",
                self.theme_settings.branch,
                self.theme_settings.repo,
                f"{self.theme_settings.get_full_directory}/{self.theme_settings.repo_name}",
            ]
        )

        if result != 0:
            raise GitCloneException(
                f"""
                Finish not success. Error `subprocess api` {result}
                There are a trouble to enable themes.
                """
            )

    def check_directory(self) -> None:
        if os.path.isdir(f"{self.theme_settings.get_full_directory}"):
            self.subprocess.call(
                ["sudo", "rm", "-rf", f"{self.theme_settings.get_full_directory}"]
            )

    def create_directory(self) -> None:
        subprocess.call(["mkdir", "-p", f"{self.theme_settings.get_full_directory}"])
