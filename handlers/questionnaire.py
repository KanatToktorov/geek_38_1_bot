from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Run🏃‍♂️ Bike🚴‍♂️ Swim🏊‍♂️ ?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )


async def run_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Running is good!\n"
             "Have you ever run a marathon?",
        reply_markup=await questionnaire_inline_buttons.run_questionnaire_keyboard()
    )

async def bike_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cycling is good!\n"
             "Do you ride a bike in winter?",
        reply_markup=await questionnaire_inline_buttons.bike_questionnaire_keyboard()
    )

async def swim_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Swimming is good!\n"
             "Is the swimming pool close to home?",
        reply_markup=await questionnaire_inline_buttons.swim_questionnaire_keyboard()
    )


async def yes_run_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool! You are a marathon runner"
    )


async def no_run_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Still to come! You will be a marathon runner"
    )

async def yes_bike_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="It must be cold"
    )


async def no_bike_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="That's right, otherwise you might catch a cold"
    )

async def yes_swim_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="It is very comfortable"
    )


async def no_swim_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool! If you go to the pool even though it is far"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        run_answer,
        lambda call: call.data == "run"
    )
    dp.register_callback_query_handler(
        yes_run_answer,
        lambda call: call.data == "yes_run"
    )
    dp.register_callback_query_handler(
        no_run_answer,
        lambda call: call.data == "no_run"
    )
    dp.register_callback_query_handler(
        bike_answer,
        lambda call: call.data == "bike"
    )
    dp.register_callback_query_handler(
        yes_bike_answer,
        lambda call: call.data == "yes_bike"
    )
    dp.register_callback_query_handler(
        no_bike_answer,
        lambda call: call.data == "no_bike"
    )
    dp.register_callback_query_handler(
        swim_answer,
        lambda call: call.data == "swim"
    )
    dp.register_callback_query_handler(
        yes_swim_answer,
        lambda call: call.data == "yes_swim"
    )
    dp.register_callback_query_handler(
        no_swim_answer,
        lambda call: call.data == "no_swim"
    )