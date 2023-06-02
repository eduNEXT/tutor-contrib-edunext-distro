import click
from tutordistro.distro.repository_validator.domain.url_validator import URLValidator
from tutordistro.distro.repository_validator.infrastructure.git_repository_checker import GitRepositoryChecker

class GitURLValidator:
    def __init__(self, package):
        self.url = self.format_public_package_url(package)

    def format_public_package_url(self, package):
        if package['index'] == 'git' and not package['private']:
            return f"https://github.com/{package['path']}/{package['repo']}/tree/{package['version']}"
        return False

    def validate(self):
        if not self._is_git_repository():
            return click.echo("Git repository " + self.url + " does not exist")
        return click.echo("Git repository " + self.url + " DONE")

    def _is_git_repository(self):
        if self.url:  
            repository_url = URLValidator(self.url)
            git_repository_checker = GitRepositoryChecker()
            return git_repository_checker.check(repository_url)
        