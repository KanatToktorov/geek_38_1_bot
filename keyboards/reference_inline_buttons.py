from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Generate Link 📎",
        callback_data="reference_link"
    )
    list_button = InlineKeyboardButton(
        "List of my referrals 📄",
        callback_data="referral_list"
    )
    markup.add(link_button)
    markup.add(list_button)
    return markup
