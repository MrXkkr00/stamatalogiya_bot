from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InputFile

from data.config import Doctors, ADMINS
from keyboards.default.Keyboards import bosh_menu_ru, bosh_m_ru
from keyboards.inline.qabul_uchun import kun, Yakubov_Dilmurod_ru, \
    Yakubov_Dilshod_ru, Lor_ru, soat_10, soat_11, soat_12, soat_14, soat_15, soat_16, soat_17, soat_18, \
    oy_10_ru, oy_1_ru, oy_2_ru, oy_12_ru, oy_11_ru, oy_9_ru, oy_8_ru, oy_7_ru, oy_6_ru, oy_5_ru, oy_4_ru, \
    oy_3_ru, qabuloddiy_ru
from loader import dp, bot
from utils.db_api.users_sql import Database_User


class Qabul_in_ru(StatesGroup):
    doctor = State()
    tanlov = State()
    oy = State()
    kun = State()
    soat = State()


@dp.message_handler(text="🏠Главное меню", state=[Qabul_in_ru.kun, Qabul_in_ru.tanlov, Qabul_in_ru.oy, Qabul_in_ru.soat, Qabul_in_ru.doctor])
async def soat_ru(message: types.Message, state: FSMContext):
    await message.answer(f"🏠Главное меню", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(text="🏠Главное меню")
async def soat112(message: types.Message):
    await message.answer(f"🏠Главное меню", reply_markup=bosh_menu_ru)


@dp.message_handler(text="📝Записаться на приём")
async def qabul1_ru(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    await state.update_data(
        {"user_id": user_id}
    )
    await message.answer(f"Выберите врача : ", reply_markup=bosh_m_ru)
    await message.answer_photo(photo=InputFile("./data/rasm/dilshod.jpg"), reply_markup=Yakubov_Dilshod_ru)
    await message.answer_photo(photo=InputFile("./data/rasm/dilmurod.jpg"), reply_markup=Yakubov_Dilmurod_ru)
    await message.answer_photo(photo=InputFile("./data/rasm/lor.jpg"), reply_markup=Lor_ru)
    await Qabul_in_ru.doctor.set()


@dp.callback_query_handler(text_contains="#", state=Qabul_in_ru.doctor)
async def location_ru(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"doctor": call.data[1:2]}
    )

    await call.message.answer(f"Выберите нужный раздел", reply_markup=qabuloddiy_ru)
    await call.message.answer(f"экстренный приём (возможен только в случай острой боли)")
    await Qabul_in_ru.tanlov.set()


@dp.callback_query_handler(text_contains="$", state=Qabul_in_ru.tanlov)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    msg = int(call.data[1:2])
    if msg == 2:
        data = await state.get_data()
        user_id = str(data.get("user_id"))

        db_user = Database_User()
        try:
            await db_user.create()
        except:
            pass

        user1 = await db_user.select_user(user_id=user_id)
        doctor = int(data.get("doctor"))
        await call.message.answer(f"Мы перезвоним вам в течение 5 минут", reply_markup=bosh_menu_ru)
        await bot.send_message(chat_id=ADMINS[doctor], text=f"📝 ❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️ \n"
                                                       f"👨‍⚕️Doctor : {Doctors[doctor]}\n"
                                                       f"🙎🏻‍♂️Mijoz : {user1[3]}\n"
                                                       f"👼Tug'ilgan sana : {user1[4]}\n"
                                                       f"☎️Number : {user1[5]}")
        await bot.send_message(chat_id=ADMINS[0], text=f"📝 ❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️ \n"
                                                       f"👨‍⚕️Doctor : {Doctors[doctor]}\n"
                                                       f"🙎🏻‍♂️Mijoz : {user1[3]}\n"
                                                       f"👼Tug'ilgan sana : {user1[4]}\n"
                                                       f"☎️Number : {user1[5]}")
        await db_user.disconnect()
        await state.finish()
    else:
        oy_son = int(strftime(f"%m", gmtime()))
        oy_keyboard = oy_10_ru
        oy_keyboard2 = oy_10_ru
        if oy_son == 1:
            oy_keyboard = oy_1_ru
            oy_keyboard2 = oy_2_ru
        if oy_son == 2:
            oy_keyboard = oy_2_ru
            oy_keyboard2 = oy_3_ru
        if oy_son == 3:
            oy_keyboard = oy_3_ru
            oy_keyboard2 = oy_4_ru
        if oy_son == 4:
            oy_keyboard = oy_4_ru
            oy_keyboard2 = oy_5_ru
        if oy_son == 5:
            oy_keyboard = oy_5_ru
            oy_keyboard2 = oy_6_ru
        if oy_son == 6:
            oy_keyboard = oy_6_ru
            oy_keyboard2 = oy_7_ru
        if oy_son == 7:
            oy_keyboard = oy_7_ru
            oy_keyboard2 = oy_8_ru
        if oy_son == 8:
            oy_keyboard = oy_8_ru
            oy_keyboard2 = oy_9_ru
        if oy_son == 9:
            oy_keyboard = oy_9_ru
            oy_keyboard2 = oy_10_ru
        if oy_son == 10:
            oy_keyboard = oy_10_ru
            oy_keyboard2 = oy_11_ru
        if oy_son == 11:
            oy_keyboard = oy_11_ru
            oy_keyboard2 = oy_12_ru
        if oy_son == 12:
            oy_keyboard = oy_12_ru
            oy_keyboard2 = oy_1_ru
        await call.message.answer(f"Выберите месяц", reply_markup=oy_keyboard)
        await call.message.answer(f"Выберите месяц", reply_markup=oy_keyboard2)
        await Qabul_in_ru.oy.set()


@dp.callback_query_handler(text_contains="0000", state=Qabul_in_ru.oy)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    oy = int(int(callback_data) / 10000)
    await state.update_data(
        {"oy": oy}
    )
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Выберите день", reply_markup=kun)
    await Qabul_in_ru.next()
    # await call.answer(cache_time=60)
    # await call.message.delete()


@dp.callback_query_handler(text_contains="99", state=Qabul_in_ru.kun)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    kun1 = int(int(callback_data) / 100)
    await state.update_data(
        {"kun": kun1}
    )
    await call.message.answer("Выберите время")

    data = await state.get_data()
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))

    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    test = 0
    oy_son = int(strftime(f"%m", gmtime()))
    kun_son = int(strftime(f"%d", gmtime()))

    if oy_son * 100 + kun_son >= oy * 100 + kun:
        await call.message.answer(f"Вы указали прошедшее время.\n"
                                  f"Пожалуйста, проверьте и введите еще раз", reply_markup=bosh_menu_ru)
        await state.finish()

    else:
        try:
            user10 = await db_user.select_user(oy=oy, day=kun, soat=10, doctor=doctor)

        except:
            user10 = []

        try:
            user11 = await db_user.select_user(oy=oy, day=kun, soat=11, doctor=doctor)
        except:
            user11 = []
        try:
            user12 = await db_user.select_user(oy=oy, day=kun, soat=12, doctor=doctor)
        except:
            user12 = []
        # try:
        #     user13 = await db_user.select_user(oy=oy, day=kun, soat=13, doctor=doctor)
        # except:
        #     user13 = []
        try:
            user14 = await db_user.select_user(oy=oy, day=kun, soat=14, doctor=doctor)
        except:
            user14 = []
        try:
            user15 = await db_user.select_user(oy=oy, day=kun, soat=15, doctor=doctor)
        except:
            user15 = []
        try:
            user16 = await db_user.select_user(oy=oy, day=kun, soat=16, doctor=doctor)
        except:
            user16 = []
        try:
            user17 = await db_user.select_user(oy=oy, day=kun, soat=17, doctor=doctor)
        except:
            user17 = []
        try:
            user18 = await db_user.select_user(oy=oy, day=kun, soat=18, doctor=doctor)
        except:
            user18 = []
        try:
            user24 = await db_user.select_user(oy=oy, day=kun, soat=24, doctor=doctor)
        except:
            user24 = None
        print(f"user24:{user24}")
        if not user24 == None:
            await call.message.answer(f"Сегодня занят. Пожалуйста, забронируйте другой день..",
                                      reply_markup=bosh_menu_ru)
            await state.finish()
        else:
            if not user10 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_10)
            if not user11:
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_11)
            if not user12 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_12)
            # if not user13 and not user24:
            #     test = 1
            #     await call.message.answer(f"Время", reply_markup=soat_13)
            if not user14 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_14)
            if not user15 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_15)
            if not user16 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_16)
            if not user17 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_17)
            if not user18 :
                test = 1
                await call.message.answer(f"Время", reply_markup=soat_18)
            if test == 0:
                await call.message.answer(f"Сегодня занят. Пожалуйста, забронируйте другой день.",
                                          reply_markup=bosh_menu_ru)
                await state.finish()
            else:
                await Qabul_in_ru.next()
    await db_user.disconnect()


@dp.callback_query_handler(text_contains="*", state=Qabul_in_ru.soat)
async def soat_ru(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    soat = int(call.data[1:])
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    user_id = str(data.get("user_id"))
    print(f"user_id: {user_id}")
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    await db_user.update_user_qabul(user_id=user_id, oy=oy, day=kun, soat=soat, doctor=doctor)
    await call.message.answer(f"Ваш запрос получен \n"
                              f"Мы ждём вас в {kun}.{oy}.2024 {soat}:00", reply_markup=bosh_menu_ru)
    user = await db_user.select_user(user_id=user_id, oy=oy, day=kun, soat=soat, doctor=doctor)
    print(user)
    try:
        doctor_number = int(user[10])
    except:
        doctor_number = 2
    await bot.send_message(chat_id=ADMINS[doctor_number], text=f"📝{user[9]}:00  {user[8]}.{user[7]}.2024  \n"
                                                   f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                                   f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                                   f"👼Tug'ilgan sana : {user[4]}\n"
                                                   f"☎️Number : {user[5]}")
    await bot.send_message(chat_id=ADMINS[0], text=f"📝{user[9]}:00  {user[8]}.{user[7]}.2024  \n"
                                                   f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                                   f"🙎🏻‍♂️Mijoz : +{user[3]}\n"
                                                   f"👼Tug'ilgan sana : {user[4]}\n"
                                                   f"☎️Number : +{user[5]}")
    await db_user.disconnect()
    await state.finish()
# Record id=3 user_id=None user_name=None full_name='Liya and 9090909' birth_day=None phone_nomer=None bonus=None oy=2 day=20 soat=10 doctor='2'
