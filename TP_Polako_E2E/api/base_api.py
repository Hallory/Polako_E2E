from urllib.parse import urlparse

import requests


class BaseApi:
    def __init__(self, base_url: str, token: str = None):
        parsed = urlparse(base_url)
        self.base_url = f"{parsed.scheme}://{parsed.netloc}"

        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
