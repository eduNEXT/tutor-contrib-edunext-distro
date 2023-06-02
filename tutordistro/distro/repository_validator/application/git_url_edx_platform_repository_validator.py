import click
from tutordistro.distro.repository_validator.domain.url_validator import URLValidator
from tutordistro.distro.repository_validator.infrastructure.git_repository_checker import GitRepositoryChecker


class GitURLEdxPlatformRepositoryValidator:
    def __init__(self, edx_platform_repository, edx_platform_version):
        self.url = self.format_edx_platform_repository_url(edx_platform_repository, edx_platform_version)

    def format_edx_platform_repository_url(self, edx_platform_repository, edx_platform_version):
        if edx_platform_repository.endswith('.git'):
            edx_platform_repository = edx_platform_repository[:-4]
        return edx_platform_repository + '/tree/' + edx_platform_version

    def validate(self):
        if not self._is_git_repository():
            return click.echo("Git repository " + self.url + " does not exist")
        return click.echo("Git repository " + self.url + " DONE")

    def _is_git_repository(self):
        git_repository_checker = GitRepositoryChecker()
        repository_url = URLValidator(self.url)
        return git_repository_checker.check(repository_url)
