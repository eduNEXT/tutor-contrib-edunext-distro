import os
import subprocess

from tutordistro.distro.domain.distro_repository import DistroRepository
from tutordistro.distro.domain.clone_exception import CloneException
from tutordistro.distro.domain.theme_settings import ThemeSettings


class DistroGitRepository(DistroRepository):

    def create_directory(self) -> None:
        pass

    def clone(self, theme_settings: type(ThemeSettings)) -> None:
        if "https" == theme_settings.settings["protocol"]:
            repo = f"https://{theme_settings.settings['domain']}/{theme_settings.settings['path']}/{theme_settings.settings['repo']}"
        elif "ssh" == theme_settings.settings["protocol"]:
            repo = f"git@{theme_settings.settings['domain']}:{theme_settings.settings['path']}/{theme_settings.settings['repo']}"

        result = subprocess.call(
            [
                "git",
                "clone",
                "-b",
                theme_settings.settings["version"],
                repo,
                f"{theme_settings.get_full_directory}",
            ]
        )

        if result != 0:
            raise CloneException(
                f"""
                Finish not success. Error `subprocess api` {result}
                There are a trouble to enable themes.
                """
            )

    def check_directory(self) -> None: pass
        # if os.path.isdir(f"{self.theme_settings.get_full_directory}"):
        #     subprocess.call(
        #         ["sudo", "rm", "-rf", f"{self.theme_settings.get_full_directory}"]
        #     )
