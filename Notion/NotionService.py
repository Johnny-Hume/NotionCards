from Notion.NotionClient import NotionClient
from Domain.NotionPage import NotionPage
import json


class NotionService:

    def __init__(self):
        self.secret = "secret_grUrCxxJSohDgwmQVYk45kS799Ie4KuDS9f6ZmtMEkn"
        self.version = "2021-08-16"
        self.base_url = "https://api.notion.com/v1/"
        self.client = self.create_client()

    def create_client(self):
        return NotionClient(
            secret=self.secret,
            version=self.version,
            base_url=self.base_url
        )

    def get_all_pages(self):
        results = self.__search__()
        return self.__convert_to_pages__(results)

    def __convert_to_pages__(self, results):
        pages = []
        for result in results:
            pages.append(
                NotionPage(
                    result["id"],
                    result["properties"]['title']["title"][0]["plain_text"]
                )
            )
        return pages

    def __search__(self):
        response = self.client.search()
        return json.loads(response.content)["results"]
