# import sqlite3
# from aiogram.utils.deep_linking import _create_link
# from aiogram import types, Dispatcher
# from config import bot, MEDIA_DESTINATION
# from database import bot_db
# from keyboards import start_inline_buttons
# import const
# from scraping.news_scraper import NewsScraper
# from scraping.async_scraper import AsyncScraper
#
# async def start_button(message: types.Message):
#     db = bot_db.Database()
#     scraper = AsyncScraper()
#     news = await scraper.get_pages()
#     news_list = []
#     for i in news:
#         news_list.extend(i)
#     if not db.sql_select_news():
#         for i in news_list[:5]:
#             db.sql_insert_news(i["link"],)
#
#     for i in news_list[-5:]:
#         text = (f'{i["link"]}')
#         await message.answer(text)
#
#
#
# def register_scraper_handlers(dp: Dispatcher):
#     dp.register_message_handler(
#         start_button,
#         commands=['scraper']
#     )
