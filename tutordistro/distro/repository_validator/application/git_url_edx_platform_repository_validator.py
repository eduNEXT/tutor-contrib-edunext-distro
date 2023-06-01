from tutordistro.distro.repository_validator.domain.url_validator import URLValidator
from tutordistro.distro.repository_validator.infrastructure.git_repository_checker import GitRepositoryChecker


class GitURLEdxPlatformRepositoryValidator:
    def __init__(self, edx_platform_repository, edx_platform_version):
        self.url = self.format_edx_platform_repository_url(edx_platform_repository, edx_platform_version)

    def format_edx_platform_repository_url(edx_platform_repository, edx_platform_version):
        if edx_platform_repository.endswith('.git'):
            edx_platform_repository = edx_platform_repository[:-4]
        return edx_platform_repository + '/tree/' + edx_platform_version

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
