from tutordistro.distro.domain.distro_repository import DistroRepository
from tutordistro.distro.domain.git_clone_exception import GitCloneException


class DistroGitRepository(DistroRepository):
    def __init__(self, theme_settings, subprocess, click):
        super.__init__(theme_settings, subprocess, click)
        self.subprocess = subprocess
        self.click = click
        self.theme_settings = theme_settings

    def clone(self) -> None:
        super().clone()
        self.click.echo(f"Clonning...")
        result = self.subprocess.call(
            [
                "git",
                "clone",
                "-b",
                self.theme_settings.branch,
                self.theme_settings.repo,
                f"{self.theme_settings.get_full_directory}/{self.theme_settings.repo_name}",
            ]
        )

        if result == 0:
            self.click.echo("Finishing...")
            self.click.echo("Themes are enable now.")
        else:
            raise GitCloneException(
                f"""
                Finish not success. Error `subprocess api` {result}
                There are a trouble to enable themes.
                """
            )

    def check_directory(self, os) -> None:
        super().check_directory(os)
        if os.path.isdir(f"{self.theme_settings.get_full_directory}"):
            self.click.echo("Cleaning old themes...")
            self.subprocess.call(
                ["sudo", "rm", "-rf", f"{self.theme_settings.get_full_directory}"]
            )

    def create_directory(self) -> None:
        super().create_directory()
        self.click.echo(f"Creating {self.theme_settings.get_full_directory}...")
        self.subprocess.call(
            ["mkdir", "-p", f"{self.theme_settings.get_full_directory}"]
        )
