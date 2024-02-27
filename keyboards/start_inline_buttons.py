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
    registration_button = InlineKeyboardButton(
        "Registration 🖊",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "My profile 📄",
        callback_data="my_profile"
    )
    profiles_button = InlineKeyboardButton(
        "View profiles 📜",
        callback_data="random_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Reference Menu 💵",
        callback_data="reference_menu"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(check_ban_button)
    markup.add(my_profile_button)
    markup.add(profiles_button)
    markup.add(reference_button)
    return markup
