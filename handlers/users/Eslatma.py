from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS, Doctors
from keyboards.inline.kon_loc import kontactlocatsiya
from loader import dp, bot
from utils.db_api.users_sql import Database_User




@dp.message_handler(text="/Eslatma", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]])
async def bonus(message: types.Message):
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    oy_son = int(strftime(f"%m", gmtime()))
    kun_son = int(strftime(f"%d", gmtime()))
    print(kun_son)
    for i in range(10, 19):
        try:
            user1 = await db_user.select_user(oy=oy_son, day=kun_son, soat=i)
            await bot.send_message(chat_id=user1[1],
                                   text=f"Ассалому алейкум! Сиз врач-стоматолог кабулига ёзилганингизни эслатиб у́тамиз.\n\n"
                                        f"Доброе утро! Напоминаем вам что вы записаны на приём к стоматологу.")
            doctor_number = int(user1[10])
            await message.answer(text=f"📝{user1[9]}:00  {user1[8]}.{user1[7]}  \n"
                                      f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                      f"🙎🏻‍♂️Mijoz : {user1[3]}\n"
                                      f"👼Tug'ilgan sana : {user1[4]}\n"
                                      f"☎️Number : +{user1[5]}")
            user1 = []
        except:
            pass
    await db_user.disconnect()

