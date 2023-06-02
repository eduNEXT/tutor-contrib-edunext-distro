import requests


class GitRepositoryChecker:
    def check(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            return False
        return True