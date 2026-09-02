class NewsArticle:
    def __init__(self, title: str, author: str):
        is_valid = self.__is_valid_title_and_author(title, author)
        if is_valid:
            self.__title = title
            self.__author = author
        else:
            self.__title = 'Без названия'
            self.__author = 'Неизвестный автор'

    def __is_valid_title_and_author(self, title: str, author: str) -> bool:
        if isinstance(title, str) and isinstance(author, str):
            if title.strip() and author.strip():
                return True
        return False

    def print(self):
        print(f'Статья "{self.__title}", опубликована автором {self.__author}')
