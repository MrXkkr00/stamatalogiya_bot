from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.config import Doctors
from handlers.users.qabul_inline import Qabul_in
from keyboards.inline.kon_loc import kontactlocatsiya, kontactlocatsiya_ru
from keyboards.inline.qabul_uchun import oy
from loader import dp
from utils.db_api.users_sql import Database_User


@dp.message_handler(text="📝Моя очередь")
async def kontact_ru(message: types.Message):
    user_id = str(message.from_user.id)
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    try:
        nul = await db_user.select_user(user_id=str(user_id))
    except:
        nul = []
    if nul:
        user = await db_user.select_user(user_id=str(user_id))
        doctor_number = int(user[10])
        await message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                             f"👨‍⚕Врач : {Doctors[doctor_number]}\n")
    else:
        await message.answer(f"Вы еще не записались на приём к врачу")
    await db_user.disconnect()


@dp.message_handler(text="📝Navbatim")
async def kontact_ru(message: types.Message):
    user_id = str(message.from_user.id)
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    try:
        nul = await db_user.select_user(user_id=user_id)
    except:
        nul = []
    if nul:
        user = await db_user.select_user(user_id=user_id)
        doctor_number = int(user[10])
        await message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}.2024  \n"
                             f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n")

    else:
        await message.answer(f"Siz hali shifakor qabuliga yozilmagansiz")
    await db_user.disconnect()
