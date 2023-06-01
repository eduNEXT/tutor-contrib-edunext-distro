import re


class URLValidator:
    def validate(self, url):
        url_pattern = re.compile(r'^https?://(www\.)?github\.com/[-\w]+/[-\w]+$')
        return bool(re.match(url_pattern, url))