import requests

class NotionClient:

    def __init__(self, secret, version, base_url):
        self.secret = secret
        self.version = version
        self.base_url = base_url
        self.headers = {"Authorization": "Bearer " + secret, "Notion-Version":version}

    def search(self):
        r = requests.post(self.base_url + "search", headers=self.headers)
        return r.content
    
    def get_page_by_id(self, page_id):
        r = requests.get(
            url=self.base_url + "pages/" + page_id,
            headers=self.headers
        )
        return r.content
    
    def get_block_children(self, block_id):
        r = requests.get(
            url=self.base_url + "blocks/" + block_id + "/children",
            headers=self.headers
        )
        return r.content
    
    def get_block_by_id(self, id):
        r = requests.get(
            url=self.base_url + "blocks/" + id,
            headers=self.headers
        )
        return r.content