from tutordistro.distro.repository_validator.domain.url_validator import URLValidator
from tutordistro.distro.repository_validator.infrastructure.git_repository_checker import GitRepositoryChecker


class GitURLValidator:
    def __init__(self, package):
        self.url = self.format_public_package_url(package)

    def format_public_package_url(package):
        if package['index'] == 'git' and not package['private']:
            return f"https://github.com/{package['path']}/{package['repo']}/tree/{package['version']}"

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