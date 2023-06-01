import re
from tutordistro.distro.repository_validator.domain.url_validator import URLValidator
from tutordistro.distro.repository_validator.infrastructure.git_repository_checker import GitRepositoryChecker


class GitURLOpenedxExtraPipRequirementsValidator:
    def __init__(self, git_url):
        self.url = self.format_git_url(git_url)

    def format_git_url(git_url):
        pattern = r"git\+(https?://\S+?)(?:#|$)"
        result = re.search(pattern, git_url)
        if result:
            # Replace '@' with '/tree/' in the URL and make the request
            return result.group(1).replace('@', '/tree/').replace('.git', '')

    def validate(self):
        if not self._is_valid_url():
            return False
        if not self._is_git_repository():
            return False
        return True

    def _is_valid_url(self):
        url_validator = URLValidator()
        return url_validator.validate(self.url)

    def _is_git_repository(self):
        git_repository_checker = GitRepositoryChecker()
        return git_repository_checker.check(self.url)
