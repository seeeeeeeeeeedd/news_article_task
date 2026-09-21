from news_article import NewsArticle


class Author:
    def __init__(self, name: str, password: str):

        is_valid = self.__is_valid_name(name)

        if is_valid:
            self.__name = name.title()
        else:
            self.__name = 'Неизвестный автор'

        self.__password = password

    def create_article(self, title: str, content: str):
        article = NewsArticle(title, content, self)
        return article

    def verify_password(self, password: str):
        if self.__password != password:
            return False
        return True

    def change_name(self, new_name: str) -> bool:
        is_valid = self.__is_valid_name(new_name)

        if is_valid:
            self.__name = new_name.title()
            return True
        else:
            return False

    def get_name(self) -> str:
        return self.__name

    def __is_valid_name(self, name: str) -> bool:

        if isinstance(name, str):
            if name.strip():
                return True
        return False
