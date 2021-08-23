from re import S
import requests

class NotionClient:

    def __init__(self, secret, version, base_url):
        self.secret = secret
        self.version = version
        self.base_url = base_url
        self.headers = {"Authorization": "Bearer " + secret, "Notion-Version":version}

    def search(self):
        r = requests.post(self.base_url + "search", headers=self.headers)
        return r