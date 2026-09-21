from author import Author


class NewsArticle:
    def __init__(self, title: str, content: str, author: Author):
        is_valid = self.__is_valid_title_and_author(title, author)

        if is_valid:
            self.__title = title.capitalize()
            self.__content = content
            self.__author = author
        else:
            self.__title = 'Без названия'
            self.__content = 'Содержание отсутствует'
            self.__author = Author('Неизвестный автор')

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content

    def get_author(self):
        return self.__author

    def __is_text_valid(self, text) -> bool:
        if not isinstance(text, str):
            return False
        if not text.strip():
            return False
        return True

    def __is_author_valid(self, author) -> bool:
        if not isinstance(author, Author):
            return False
        if not author.get_name():
            return False
        return True
