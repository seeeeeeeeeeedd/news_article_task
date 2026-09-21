from news_article import NewsArticle


class Author:
    def __init__(self, name: str):
        is_valid = self.__is_valid_name(name)

        if is_valid:
            self.__name = name.title()
        else:
            self.__name = 'Неизвестный автор'

    def create_article(self, title: str):
        article = NewsArticle(title, self.get_name())
        return article

    def get_name(self) -> str:
        return self.__name

    def __is_valid_name(self, name: str) -> bool:

        if isinstance(name, str):
            if name.strip():
                return True
        return False
