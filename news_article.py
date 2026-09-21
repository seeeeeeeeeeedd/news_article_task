from author import Author


class NewsArticle:
    def __init__(self, title: str, author: Author):
        is_valid = self.__is_valid_title_and_author(title, author)

        if is_valid:
            self.__title = title.capitalize()
            self.__author = author
        else:
            self.__title = 'Без названия'
            self.__author = 'Неизвестный автор'

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def __is_valid_title_and_author(self, title: str, author: Author) -> bool:

        if isinstance(title, str) and isinstance(author, Author):
            if title.strip() and author.get_name():
                return True
        return False
