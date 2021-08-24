import sqlite3 as sql
from Domain import FlashCard


class FlashCardRepository:

    def __init__(self):
        self.con = sql.connect("Notion-Cards.db")

    def create_flash_cards_table(self):
        with self.con:
            self.con.execute("""
                                CREATE TABLE IF NOT EXISTS FLASH_CARDS (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    question TEXT,
                                    answer TEXT
                                );
                            """)

    def insert_flash_card_into_flash_cards_table(self, flashCard):
        query = "INSERT INTO FLASH_CARDS (question, answer) VALUES(?, ?)"
        data = [flashCard.question, flashCard.answer]
        print(data)
        with self.con:
            self.con.execute(query, data)
