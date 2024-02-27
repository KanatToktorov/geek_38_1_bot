import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_buttons
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup

class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    marital_status = State()
    address = State()
    photo = State()

async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send me your Nickname, please!"
    )
    await RegistrationStates.nickname.set()

async def load_nickname (message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)



    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me your Biography!'
    )
    await RegistrationStates.next()

async def load_bio(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="How old are you?\n"
            "(Send me only numeric text)\n"
            "Example: 27 or 29"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                        state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="I told you send me ONLY numeric text\n"
                 "Registration failed❌\n"
                 "Restart registration!!!"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = int(message.text)
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your zodiac sign"
    )
    await RegistrationStates.next()


async def load_zodiac_sign (message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['zodiac_sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your marital_status"
    )
    await RegistrationStates.next()

async def load_marital_status(message: types.Message,
                            state: FSMContext):
    async with state.proxy() as data:
        data['marital_status'] = message.text
        print(data)


    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your address"
    )
    await RegistrationStates.next()

async def load_address(message: types.Message,
                                state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your photo\n"
            "Only in photo format"
    )
    await RegistrationStates.next()

async def load_photo (message: types.Message,
                         state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir = MEDIA_DESTINATION
    )
    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            zodiac_sign=data['zodiac_sign'],
            marital_status=data['marital_status'],
            address=data['address'],
            photo=path.name
        )

        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    zodiac_sign=data['zodiac_sign'],
                    marital_status=data['marital_status'],
                    address=data['address'],
                )
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="You are successfully registered👏\n"
            "Congratulations!!!"
    )
    await state.finish()






def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == 'registration'
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_marital_status,
        state=RegistrationStates.marital_status,
        content_types=['text']
    )
    dp.register_message_handler(
        load_address,
        state=RegistrationStates.address,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
