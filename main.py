from news_portal import NewsPortal
from author import Author

commands = {
    '1': 'Создать и опубликовать статью',
    '2': 'Добавить автора',
    '3': 'Посмотреть все статьи',
    '4': 'Посмотреть всех авторов',
    '5': 'Посмотреть все статьи определенного автора',
    '0': 'Выйти из программы'
}

(CREATE_AND_PUBLISH_ARTICLE_COMMAND, ADD_AUTHOR_COMMAND, SHOW_ALL_ARTICLES_COMMAND,
 SHOW_ALL_AUTHORS_COMMAND, SHOW_ARTICLES_BY_AUTHOR_COMMAND, EXIT_COMMAND) = commands.keys()

news_portal = NewsPortal()

is_program_running = True
while is_program_running:

    for command_number, command in commands.items():
        print(f'{command_number}: {command}')

    user_number = input('Выберете действие и укажите его номер: ')

    if user_number in commands.keys():
        if user_number == CREATE_AND_PUBLISH_ARTICLE_COMMAND:
            user_author_name = input('Укажите имя автора: ')
            current_author_name = news_portal.find_author_by_name(user_author_name)

            if current_author_name == None:
                current_author_name = Author(user_author_name)
                news_portal.add_author(current_author_name)
            user_article_title = input('Укажите название статьи: ')

            article = current_author_name.create_article(user_article_title)
            news_portal.publish_article(article)

        elif user_number == ADD_AUTHOR_COMMAND:
            user_author_name = input('Укажите имя автора: ')
            current_author_name = news_portal.find_author_by_name(user_author_name)

            if current_author_name == None:
                current_author_name = Author(user_author_name)
                news_portal.add_author(current_author_name)
                print('Автор успешно добавлен')
            else:
                print('Такой автор уже существует')
        elif user_number == SHOW_ALL_ARTICLES_COMMAND:
            news_portal.show_published_articles()
        elif user_number == SHOW_ALL_AUTHORS_COMMAND:
            news_portal.show_authors()
        elif user_number == SHOW_ARTICLES_BY_AUTHOR_COMMAND:
            user_author_name = input('Введи имя автора для поиска: ')
            news_portal.show_articles_by_author(user_author_name)
        elif user_number == EXIT_COMMAND:
            print('Выход из программы.')
            is_program_running = False
    else:
        print('Такой команды не существует. Попробуйте снова')
