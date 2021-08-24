class FlashCardService:

    def __init__(self, question_marker, answer_marker):
        self.question_marker = question_marker
        self.answer_marker = answer_marker

    def get_question_from_block_content(self, block_content):
        return self.__get_text_between_markers__(block_content, self.question_marker)

    def get_answer_from_block_content(self, block_content):
        return self.__get_text_between_markers__(block_content, self.answer_marker)

    def get_question_from_block_content_rem(self, block_content):
        if block_content == None:
            return
        first_colon_index = block_content.find(':')
        if block_content[first_colon_index + 1] == ':':
            return block_content[: first_colon_index].strip()
        return None

    def get_answer_from_block_content_rem(self, block_content):
        if block_content == None:
            return
        first_colon_index = block_content.find(':')
        if block_content[first_colon_index + 1] == ':':
            return block_content[first_colon_index + 2:].strip()
        return None


    def __get_text_between_markers__(self, block_content, marker):
        if block_content == None:
            return
        start_marker_index = block_content.find(marker)
        end_marker_index = block_content[start_marker_index + 1:].find(marker) + start_marker_index
        if start_marker_index == -1 or end_marker_index == -1:
            return None
        return block_content[start_marker_index + 1:end_marker_index + 1]
