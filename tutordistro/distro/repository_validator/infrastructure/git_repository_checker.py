import requests


class GitRepositoryChecker:
    def check(self, url):
        try:
            response = requests.get(url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False