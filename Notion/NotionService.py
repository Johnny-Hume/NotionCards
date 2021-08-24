from Notion.NotionClient import NotionClient
from Domain.NotionPage import NotionPage
from Domain.NotionBlock import NotionBlock
import json


class NotionService:

    def __init__(self):
        self.secret = "secret_grUrCxxJSohDgwmQVYk45kS799Ie4KuDS9f6ZmtMEkn"
        self.version = "2021-08-16"
        self.base_url = "https://api.notion.com/v1/"
        self.client = self.__create_client__()

    def get_all_pages(self):
        search_results = self.__search__()
        return self.__convert_to_pages__(search_results)

    def get_page_by_id(self, page_id):
        page = self.client.get_page_by_id(page_id)
        return page

    def get_blocks_by_id(self, id):
        content = self.__get_block_children__(id)
        return self.__convert_to_blocks__(content["results"])

    def get_all_block_ids_on_page(self, id):
        content = self.__get_block_children__(id)
        blocks = []
        for block in content["results"]:
            blocks.append(block["id"])
            if block["has_children"]:
                blocks += self.get_all_block_ids_on_page(block["id"])
        return blocks

    def get_block_content_by_id(self, id):
        block = self.__get_block_by_id__(id)
        return block.content

    def __get_block_by_id__(self, id):
        content = self.client.get_block_by_id(id)
        block = json.loads(content)
        return self.__convert_to_block__(block)

    def __get_block_children__(self, page_id):
        content = self.client.get_block_children(page_id)
        return json.loads(content)

    def __convert_to_blocks__(self, results):
        blocks = []
        for result in results:
            blocks.append(
                self.__convert_to_block__(result)
            )
        return blocks

    def __convert_to_block__(self, result):
        block_type = result["type"]
        is_child_page = block_type == "child_page"
        text_size = 0 if is_child_page else len(result[block_type]["text"])
        text_is_empty = text_size == 0
        content = None if is_child_page or text_is_empty else result[
            block_type]["text"][0]["plain_text"]
        return NotionBlock(
            id=result["id"], block_type=block_type, content=content, has_children=result["has_children"]
        )

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
        return json.loads(response)["results"]

    def __create_client__(self):
        return NotionClient(
            secret=self.secret,
            version=self.version,
            base_url=self.base_url
        )
