import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # Загрузка страницы с документацией для Python четвёртой версии.
    response = requests.get('https://docs.python.org/4/')
    # Создание "супа" из веб-страницы.
    soup = BeautifulSoup(response.text, features='lxml')
    # Печать "супа".
    print(soup)
    # Печать "супа" с отступами.
    print(soup.prettify())
    # Печать содержимого только тега <body>.
    print(soup.html.body.prettify())
