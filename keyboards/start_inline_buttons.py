from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire 🗒️",
        callback_data="start_questionnaire"
    )
    check_ban_button = InlineKeyboardButton(
        "Check ban ✔",
        callback_data="start_check"
    )
    markup.add(questionnaire_button)
    markup.add(check_ban_button)
    return markup
