
import sqlite3

# import requests
#
#
# class NewsScraper:
#     PLUS_URL = 'https://24.kg/'
#     URL = 'https://24.kg/'
#     HEADERS = {
#         "Accept-Language":
#             "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
#     }
#
#     LINK_XPATH = '//div[@class="title"]/a/@href'
#
#     def scrape_data(self):
#         try:
#             response = requests.get(self.URL, headers=self.HEADERS)
#             response.raise_for_status()  # Проверка на ошибку при запросе
#             tree = Selector(text=response.text)
#             links = tree.xpath(self.LINK_XPATH).getall()
#
#             if links:  # Проверка наличия ссылок
#                 for link in links:
#                     print(self.PLUS_URL + link)
#             else:
#                 print("Ссылки не найдены.")
#         except requests.exceptions.RequestException as e:
#             print("Произошла ошибка при отправке запроса:", e)
#         except Exception as e:
#             print("Произошла ошибка:", e)
#
#
# if __name__ == "__main__":
#     scraper = NewsScraper()
#     scraper.scrape_data()


import requests
from parsel import Selector


class NewsScraper:
    PLUS_URL = 'https://24.kg/'
    URL = 'https://24.kg/'
    HEADERS = {
        "Accept-Language":
            "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
    }

    LINK_XPATH = '//div[@class="title"]/a/@href'


    def scrape_data(self):
        response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
        print(response.text)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()

        for link in links:
            print(self.PLUS_URL + link)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()


import sqlite3

import sqlite3

# Определяем имя новой базы данных
db_name = "create.db"

# Создаем подключение к базе данных
conn = sqlite3.connect(db_name)
cur = conn.cursor()

# Создаем таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS News
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 link TEXT)''')

# Вставляем данные в таблицу
data_to_insert = [
    "https://example.com/news1",
    "https://example.com/news2",
    "https://example.com/news3"
]

for link in data_to_insert:
    cur.execute("INSERT INTO News (link) VALUES (?)", (link,))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print(f"База данных {db_name} успешно создана и заполнена.")


import sqlite3
from database import bot_db
import requests
from parsel import Selector
import sqlite3

class DbManager:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cur = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    def create_table(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS News
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 link TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")

    def insert_data(self, data):
        try:
            for link in data:
                self.cur.execute("INSERT INTO News (link) VALUES (?)", (link,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при вставке данных: {e}")

class DbManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS News
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             link TEXT)''')
        self.conn.commit()

    def insert_data(self, data):
        for link in data:
            self.cur.execute("INSERT INTO News (link) VALUES (?)", (link,))
        self.conn.commit()
class NewsScraper:
    PLUS_URL = 'https://24.kg/'
    URL = 'https://24.kg/'
    HEADERS = {
        "Accept-Language":
            "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
    }

    LINK_XPATH = '//div[@class="title"]/a/@href'

    def scrape_data(self):
        response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        return [self.PLUS_URL + link for link in links[:5]]

if __name__ == "__main__":
    scraper = NewsScraper()
    news_data = scraper.scrape_data()
    print("Список первых пяти новостей:")
    for link in news_data:
        print(link)
    db_manager = DbManager('news.db')  # создание экземпляра класса DbManager
    db_manager.insert_data(news_data)
