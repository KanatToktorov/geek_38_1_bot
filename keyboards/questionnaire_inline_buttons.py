from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    run_button = InlineKeyboardButton(
        "Run🏃‍",
        callback_data="run"
    )
    bike_button = InlineKeyboardButton(
        "Bike🚴‍",
        callback_data="bike"
    )
    swim_button = InlineKeyboardButton(
        "Swim🏊‍♂️",
        callback_data="swim"
    )
    markup.add(run_button)
    markup.add(bike_button)
    markup.add(swim_button)
    return markup


async def run_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    run_yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_run"
    )
    run_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_run"
    )
    markup.add(run_yes_button)
    markup.add(run_no_button)
    return markup


async def bike_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    bike_yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_bike"
    )
    bike_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_bike"
    )
    markup.add(bike_yes_button)
    markup.add(bike_no_button)
    return markup


async def swim_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    swim_yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_swim"
    )
    swim_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_swim"
    )
    markup.add(swim_yes_button)
    markup.add(swim_no_button)
    return markup
