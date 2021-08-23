from Domain.NotionPage import NotionPage
from Notion.NotionService import NotionService

service = NotionService()

pages = service.get_all_pages()

for page in pages:
    print("\nPage ID: " + page.id)
    print("Page Title: " + page.title)
print("")