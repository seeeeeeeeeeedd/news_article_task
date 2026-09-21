from news_article import NewsArticle
from author import Author


class NewsPortal:
    def __init__(self):
        self.__published_articles = []
        self.__authors = []

    def publish_article(self, author, title, content):
        is_valid_author = self.__is_valid_author(author)

        if is_valid_author:
            article = author.create_article(title, content)
            current_title = article.get_title()
            current_author_name = author.get_name()
            print(f'Статья "{current_title}", опубликована автором - {current_author_name}')
            self.__published_articles.append(article)
        else:
            print('Ошибка. Некорректные данные')
            return

    def show_published_articles(self):
        for article in self.__published_articles:
            current_title = article.get_title()
            current_author = article.get_author().get_name()
            print(f'Статья "{current_title}", автор - {current_author}')

    def show_authors(self):
        for author in self.__authors:
            current_author = author.get_name()
            print(f'Автор: {current_author}')

    def add_author(self, author):
        is_valid_author = self.__is_valid_author(author)

        if is_valid_author:
            self.__authors.append(author)
        else:
            print('Ошибка. Некорректные данные')
            return

    def find_author_by_name(self, name: str) -> Author | None:
        for author in self.__authors:
            current_author_name = author.get_name()

            if current_author_name.lower() == name.lower():
                return author
        return None

    def show_articles_by_author(self, search_author):
        is_article_found = False

        for article in self.__published_articles:
            current_author_name = article.get_author().get_name()

            if current_author_name.lower() == search_author.lower():
                current_title = article.get_title()
                print(f'Статья: "{current_title}"')
                is_article_found = True

        if not is_article_found:
            print('Совпадений не найдено')

    def __is_valid_author(self, author):
        return isinstance(author, Author)

    def __is_valid_article(self, article):
        return isinstance(article, NewsArticle)
