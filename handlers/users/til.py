from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from handlers.users.qabul import Qabul_State
from handlers.users.qabul_RU import Qabul_State_ru

from keyboards.default.Keyboards import bosh_menu, bosh_menu_ru
from loader import dp
from utils.db_api.users_sql import Database_User

db_user = Database_User()


@dp.message_handler(text="🇺🇿Uzbek")
async def bot_start(message: types.Message):
    user_id = (str(message.from_user.id))
    try:
        await db_user.create()
    except:
        pass

    try:
        await db_user.create_table_users()
    except:
        pass
    try:
        user = await db_user.select_user(user_id=user_id)
        # print("try")
        # print(user)
    except:
        # print("exc")
        user = None
    await db_user.disconnect()
    if user == None:
        await message.answer(f"Assalomu Alaykum!\nSiz ro'yxatdan o'tishingiz kerak")
        await message.answer(f"Ismingizni kiriting  : ", reply_markup=ReplyKeyboardRemove())
        await Qabul_State.ism.set()
    else:
        await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


@dp.message_handler(text="🇷🇺Русский")
async def bot_start_ru(message: types.Message):
    user_id = str(message.from_user.id)
    try:
        await db_user.create()
    except:
        pass
    try:
        await db_user.create_table_users()
    except:
        pass
    try:
        user = await db_user.select_user(user_id=user_id)
        # print("try")
    except:
        # print("exc")
        user = None
    await db_user.disconnect()
    if user == None:
        await message.answer(f"Здравствуйте!\nВы должны зарегистрироваться")
        await message.answer(f"Введите ваше имя  : ", reply_markup=ReplyKeyboardRemove())
        await Qabul_State_ru.ism.set()
    else:
        # print(f"else:{user}")
        await message.answer(f"Здравствуйте!", reply_markup=bosh_menu_ru)
