import re

import click

from tutordistro.distro.repository_validator.domain.url_validator import URLValidator
from tutordistro.distro.repository_validator.infrastructure.git_repository_checker import GitRepositoryChecker


class GitURLOpenedxExtraPipRequirementsValidator:
    def __init__(self, git_url):
        self.url = git_url

    def format_git_url(self):
        pattern = r"git\+(https?://\S+?)(?:#|$)"
        result = re.search(pattern, self.url)
        if result:
            self.url = result.group(1).replace('@', '/tree/').replace('.git', '')
            # Replace '@' with '/tree/' in the URL and make the request
            return True
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
    