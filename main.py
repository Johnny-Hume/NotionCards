from FlashCard.FlashCardRepository import FlashCardRepository
from FlashCard.FlashCardService import FlashCardService
from Domain.NotionPage import NotionPage
from Notion.NotionService import NotionService
from FlashCard.FlashCardService import FlashCardService
from FlashCard.FlashCardRepository import FlashCardRepository
from Domain.FlashCard import FlashCard

service = NotionService()

fs_service = FlashCardService('<', '>')

db = FlashCardRepository()

db.create_flash_cards_table()

print("Getting all pages")
pages = service.get_all_pages()

print("Searching for possible flashcards...")
all_blocks = service.get_all_block_ids_on_page(pages[0].id)

for block in all_blocks:
        text = service.get_block_content_by_id(block)
        question = fs_service.get_question_from_block_content_rem(text)
        answer = fs_service.get_answer_from_block_content_rem(text)

        if question != None and answer != None:
            print("FlashCard Found!\nSaving to Database")
            card = FlashCard(question, answer)
            db.insert_flash_card_into_flash_cards_table(card)