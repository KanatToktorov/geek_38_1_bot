from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def check_keyboard():
    markup = InlineKeyboardMarkup()
    check_button = InlineKeyboardButton(
        "Check",
        callback_data="check"
    )
    markup.add(check_button)
    return markup