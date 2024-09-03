import json
from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InputFile

from data.config import Doctors, ADMINS
from keyboards.default.Keyboards import bosh_m, bosh_menu
from keyboards.inline.qabul_uchun import kun, oy_1, oy_2, oy_4, oy_3, oy_5, oy_6, oy_7, oy_8, oy_9, oy_10, oy_11, oy_12, \
    Yakubov_Dilshod, Yakubov_Dilmurod, Lor, soat_10, soat_14, soat_15, \
    soat_16, soat_12,  soat_11, soat_17, soat_18, qabuloddiy
from loader import dp, bot
from utils.db_api.users_sql import Database_User


class Qabul_in(StatesGroup):
    doctor = State()
    tanlov = State()
    oy = State()
    kun = State()
    soat = State()


@dp.message_handler(text="🏠Bosh Menu", state=[Qabul_in.kun, Qabul_in.oy, Qabul_in.soat, Qabul_in.tanlov, Qabul_in.doctor])
async def soat12(message: types.Message, state: FSMContext):
    await message.answer(f"🏠Bosh Menu.", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="🏠Bosh Menu")
async def soat112(message: types.Message):
    await message.answer(f"🏠Bosh Menu", reply_markup=bosh_menu)


@dp.message_handler(text="📝Qabulga yozilish")
async def qabul1(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    await state.update_data(
        {"user_id": user_id}
    )
    await message.answer(f"Doctorni tanlang : ", reply_markup=bosh_m)
    await message.answer_photo(photo=InputFile("./data/rasm/dilshod.jpg"), reply_markup=Yakubov_Dilshod)
    await message.answer_photo(photo=InputFile("./data/rasm/dilmurod.jpg"), reply_markup=Yakubov_Dilmurod)
    await message.answer_photo(photo=InputFile("./data/rasm/lor.jpg"), reply_markup=Lor)
    await Qabul_in.doctor.set()


@dp.callback_query_handler(text_contains="#", state=Qabul_in.doctor)
async def location_ru(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"doctor": call.data[1:2]}
    )

    await call.message.answer(f"Kerakli bo'limni tanlang", reply_markup=qabuloddiy)
    await call.message.answer(f"Navbatsiz qabulga yozilish (faqat o'tkir og'riqda mumkin)")

    await Qabul_in.tanlov.set()


@dp.callback_query_handler(text_contains="$", state=Qabul_in.tanlov)
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

        user = await db_user.select_user(user_id=user_id)
        doctor = int(data.get("doctor"))
        await call.message.answer(f"Biz sizga 5 minut mobaynida qo'ng'iroq qilamiz", reply_markup=bosh_menu)
        await bot.send_message(chat_id=ADMINS[doctor], text=f"📝 ❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️ \n"
                                                       f"👨‍⚕️Doctor : {Doctors[doctor]}\n"
                                                       f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                                       f"👼Tug'ilgan sana : {user[4]}\n"
                                                       f"☎️Number : {user[5]}")
        await bot.send_message(chat_id=ADMINS[0], text=f"📝 ❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️ \n"
                                                       f"👨‍⚕️Doctor : {Doctors[doctor]}\n"
                                                       f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                                       f"👼Tug'ilgan sana : {user[4]}\n"
                                                       f"☎️Number : {user[5]}")
        await db_user.disconnect()
        await state.finish()
    else:
        oy_son = int(strftime(f"%m", gmtime()))
        oy_keyboard = oy_10
        oy_keyboard2 = oy_10
        if oy_son == 1:
            oy_keyboard = oy_1
            oy_keyboard2 = oy_2
        if oy_son == 2:
            oy_keyboard = oy_2
            oy_keyboard2 = oy_3
        if oy_son == 3:
            oy_keyboard = oy_3
            oy_keyboard2 = oy_4
        if oy_son == 4:
            oy_keyboard = oy_4
            oy_keyboard2 = oy_5
        if oy_son == 5:
            oy_keyboard = oy_5
            oy_keyboard2 = oy_6
        if oy_son == 6:
            oy_keyboard = oy_6
            oy_keyboard2 = oy_7
        if oy_son == 7:
            oy_keyboard = oy_7
            oy_keyboard2 = oy_8
        if oy_son == 8:
            oy_keyboard = oy_8
            oy_keyboard2 = oy_9
        if oy_son == 9:
            oy_keyboard = oy_9
            oy_keyboard2 = oy_10
        if oy_son == 10:
            oy_keyboard = oy_10
            oy_keyboard2 = oy_11
        if oy_son == 11:
            oy_keyboard = oy_11
            oy_keyboard2 = oy_12
        if oy_son == 12:
            oy_keyboard = oy_12
            oy_keyboard2 = oy_1
        await call.message.answer(f"Oyni tanlang", reply_markup=oy_keyboard)
        await call.message.answer(f"Oyni tanlang", reply_markup=oy_keyboard2)
        await Qabul_in.oy.set()


@dp.callback_query_handler(text_contains="0000", state=Qabul_in.oy)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    oy1 = int(int(callback_data) / 10000)
    await state.update_data(
        {"oy": oy1}
    )
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Kunni tanlang", reply_markup=kun)
    await Qabul_in.next()
    # await call.answer(cache_time=60)
    # await call.message.delete()


@dp.callback_query_handler(text_contains="99", state=Qabul_in.kun)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    kun1 = int(int(callback_data) / 100)
    await state.update_data(
        {"kun": kun1}
    )
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Vaqtni tanlang")
    data = await state.get_data()
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    user_id = str(data.get("user_id"))
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass

    test = 0
    oy_son = int(strftime(f"%m", gmtime()))
    kun_son = int(strftime(f"%d", gmtime()))-1

    if oy_son * 100 + kun_son >= oy * 100 + kun:
        await call.message.answer(f"Siz o'tib ketgan vaqtni belgiladingiz.\n"
                                  f"Iltimos tekshirib qaytadan kiriting", reply_markup=bosh_menu)
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
        # print(f"user24:{user24}")
        
        
        if not  user24 == None:
            await call.message.answer(f"Bu kun band Iltimos boshqa kunga yoziling..", reply_markup=bosh_menu)
            await state.finish()

        else:
            if not user10:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_10)
            if not user11:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_11)
            if not user12:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_12)
            # if not user13 and not user24:
            #     test = 1
            #     await call.message.answer(f"Soat", reply_markup=soat_13)
            if not user14:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_14)
            if not user15:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_15)
            if not user16:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_16)
            if not user17:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_17)
            if not user18:
                test = 1
                await call.message.answer(f"Soat", reply_markup=soat_18)
            if test == 0:
                await call.message.answer(f"Bu kun band Iltimos boshqa kunga yoziling.", reply_markup=bosh_menu)
                await state.finish()
            else:
                await Qabul_in.next()


@dp.callback_query_handler(text_contains="*", state=Qabul_in.soat)
async def soat(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    soat = int(call.data[1:])
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    user_id = str(data.get("user_id"))

    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass

    await db_user.update_user_qabul(user_id=user_id, oy=oy, day=kun, soat=soat, doctor=doctor)
    await call.message.answer(f"Sizning so'rovingiz qabul qilindi \n"
                              f"Sizni {kun}.{oy}.2024 kuni soat {soat}:00 da kutamiz", reply_markup=bosh_menu)
    user = await db_user.select_user(user_id=user_id, oy=oy, day=kun, soat=soat, doctor=doctor)
    try:
        doctor_number = int(user[10])
    except:
        doctor_number = 2
    await bot.send_message(chat_id=ADMINS[doctor_number], text=f"📝{user[9]}:00  {user[8]}.{user[7]}.2024  \n"
                                                   f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                                   f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                                   f"👼Tug'ilgan sana : {user[4]}\n"
                                                   f"☎️Number : +{user[5]}")
    await bot.send_message(chat_id=ADMINS[0], text=f"📝{user[9]}:00  {user[8]}.{user[7]}.2024  \n"
                                                   f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                                   f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                                   f"👼Tug'ilgan sana : {user[4]}\n"
                                                   f"☎️Number : +{user[5]}")
    await db_user.disconnect()
    await state.finish()
