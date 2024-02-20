import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database.bot_db import Database
from keyboards import start_inline_buttons
import const

async def check_ban(call: types.CallbackQuery):
    db=Database()
    user=db.sql_select_ban_user(call.from_user.id)
    if not user:
        text=const.NO_BAN_TEXT
        await call.message.answer(text=text)
    else:
        text=const.YES_BAN_TEXT.format(count=user['count'])
        await call.message.answer(text=text)

def register_check_ban_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        check_ban,
        lambda call: call.data == 'start_check'
    )