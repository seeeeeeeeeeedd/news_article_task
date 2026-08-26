class NewsArticle:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def __is_valid_title_and_author(self, title: str, author: str) -> bool:
        if isinstance(title, str) and isinstance(author, str):
            if title.strip() and author.strip():
                return True
        return False
