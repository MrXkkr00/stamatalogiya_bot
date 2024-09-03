from data.config import Doctors, ADMINS
from handlers.users import admin
import json
from time import strftime, gmtime
from keyboards.default.Keyboards import admin_menu, admin_admin, bosh_menu, davom
from loader import bot

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.qabul_uchun import kun, Yakubov_Dilmurod_ru, \
    Yakubov_Dilshod_ru, Lor_ru, oy, Yakubov_Dilshod, Yakubov_Dilmurod, Lor, soat_18, soat_17, soat_16, soat_15, soat_14, \
    soat_12, soat_11, soat_10, alll
from loader import dp
from utils.db_api.users_sql import Database_User


class Band_qilish(StatesGroup):
    mijoz = State()
    doctor = State()
    oy = State()
    kun = State()
    davom_1 =State()
    soat = State()


@dp.message_handler(text="/admin",
                    state=[Band_qilish.mijoz, Band_qilish.doctor, Band_qilish.oy, Band_qilish.kun, Band_qilish.soat])
async def adminin(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=admin_menu)
    await state.finish()

@dp.message_handler(text="/start",
                    state=[Band_qilish.mijoz, Band_qilish.doctor, Band_qilish.oy, Band_qilish.kun, Band_qilish.soat])
async def ad4324nin(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="/band_qilish")
async def mijoz(message: types.Message):
    await message.answer(f"Mijoz haqida text\n"
                         f"F.I.SH va phone nomer", reply_markup=admin_admin)
    await Band_qilish.mijoz.set()


@dp.message_handler(state=Band_qilish.mijoz)
async def band_qilish(message: types.Message, state: FSMContext):
    await state.update_data(
        {"mijoz": message.text}
    )
    await message.answer(f"Doctorni tanlang : ")
    await message.answer_photo(photo=InputFile("./data/rasm/dilshod.jpg"), reply_markup=Yakubov_Dilshod)
    await message.answer_photo(photo=InputFile("./data/rasm/dilmurod.jpg"), reply_markup=Yakubov_Dilmurod)
    await message.answer_photo(photo=InputFile("./data/rasm/lor.jpg"), reply_markup=Lor)
    await Band_qilish.doctor.set()


@dp.callback_query_handler(text_contains="#", state=Band_qilish.doctor)
async def location_ru(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"doctor": call.data[1:2]}
    )
    await call.message.answer(f"Oyni tanlang", reply_markup=oy)
    await Band_qilish.next()


@dp.callback_query_handler(text_contains="0000", state=Band_qilish.oy)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    oy1 = int(int(callback_data) / 10000)
    await state.update_data(
        {"oy": oy1}
    )
    await call.message.answer("Kunni tanlang", reply_markup=kun)
    await Band_qilish.next()


@dp.callback_query_handler(text_contains="99", state=Band_qilish.kun)
async def buy_c23251es(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    kun1 = int(int(callback_data) / 100)
    await state.update_data(
        {"kun": kun1}
    )
    await call.message.answer("Mijozlar :")
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
        user24 = []


    if user10:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=10, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if user11:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=11, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if user12:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=12, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    # if user13:
    #     test = 1
    #     user = await db_user.select_user(oy=oy, day=kun, soat=13, doctor=doctor)
    #     doctor_number = int(user[10])
    #     await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
    #                               f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
    #                               f"🙎🏻‍♂️Mijoz : {user[3]}\n"
    #                               f"👼Tug'ilgan sana : {user[4]}\n"
    #                               f"☎️Number : {user[5]}")
    if user14:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=14, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if user15:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=15, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if user16:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=16, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if user17:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=17, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if user18:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=18, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)

    if user24:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=24, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}", reply_markup=davom)
    if test == 0:
        await call.message.answer(f"Сегодня никого нет.", reply_markup=davom)
    await db_user.disconnect()
    await Band_qilish.davom_1.set()


@dp.message_handler(text="Davom ettirish", state=Band_qilish.davom_1)
async def buy412rewes(message: types.Message, state: FSMContext):
    await message.answer("Vaqtni tanlang", reply_markup=admin_admin)
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
    kun_son = int(strftime(f"%d", gmtime()))-1

    if oy_son * 100 + kun_son >= oy * 100 + kun:
        await message.answer(f"Siz o'tib ketgan vaqtni belgiladingiz.\n"
                                  f"Iltimos tekshirib qaytadan kiriting", reply_markup=admin_admin)
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

        
        
        if not  user24 == None:
            await message.answer(f"Bu kun to'liq band", reply_markup=admin_admin)
            await state.finish()


        else:
            if not user10:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_10)
            if not user11:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_11)
            if not user12:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_12)

            if not user14:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_14)
            if not user15:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_15)
            if not user16:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_16)
            if not user17:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_17)
            if not user18:
                test = 1
                await message.answer(f"Soat", reply_markup=soat_18)
            if test == 0:
                await message.answer(f"Bu kun to'liq band.", reply_markup=admin_admin)
                await state.finish()
            else:
                await Band_qilish.soat.set()









@dp.message_handler(
    lambda message: message.text[:2].isdigit() and message.text[2] == "-" and message.text[3:5].isdigit(),
    state=Band_qilish.soat)
async def soat2ta(message: types.Message, state: FSMContext):
    msg = message.text
    soat1 = int(msg[:2])
    soat2 = int(msg[3:5])
    data = await state.get_data()
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    mijoz = "Admin + " + (data.get("mijoz"))

    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=int(soat1), doctor=doctor)
    await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=int(soat2), doctor=doctor)
    if soat2 - soat1 > 1:
        soat3 = soat1 + 1
        await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=int(soat3), doctor=doctor)
        if soat2 - soat3 > 1:
            soat4 = soat1 + 2
            await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=int(soat4), doctor=doctor)
            if soat2 - soat4 > 1:
                soat5 = soat1 + 3
                await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=int(soat5), doctor=doctor)

    await message.answer(f"Siz  {mijoz} ga "
                         f"{kun}.{oy} kuni  "
                         f"soat {soat1}:00 dan {soat2 + 1}:00 gacha \n"
                         f"band qildingiz")

    await bot.send_message(chat_id=ADMINS[1], text=f"Admin  {mijoz} ga "
                                                   f"{kun}.{oy} kuni  "
                                                   f"soat {soat1}:00 dan {soat2 + 1}:00 gacha \n"
                                                   f"band qildi")
    await db_user.disconnect()
    await state.finish()


@dp.callback_query_handler(text_contains="*", state=Band_qilish.soat)
async def soat(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    soat = int(call.data[1:])
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    mijoz = (data.get("mijoz"))

    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    if soat == 24:
        await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=24, doctor=doctor)
    else:
        await db_user.add_user(full_name=mijoz, oy=oy, day=kun, soat=soat, doctor=doctor)
    await call.message.answer(f"Siz {kun}.{oy} soat {soat} \n"
                              f"ni band qildingiz")
    await db_user.disconnect()
    await state.finish()


# text_contains="delet",
@dp.message_handler(lambda msg: msg.text[5:7].isdigit() and "delet" in msg.text ,state=Band_qilish.soat)
async def deletsoat(message: types.Message, state: FSMContext):
    msg = int(message.text[5:7])
    data = await state.get_data()
    soat = msg
    doctor = str(data.get("doctor"))
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    db = Database_User()
    print(msg, f"\n ", oy, f"\n", kun, f"\n ", soat, f"\n ", doctor)
    await db.create()
    try:
        user = await db.select_user(doctor=doctor, oy=oy, day=kun, soat=soat)
        idd = user[0]
        await db.update_id(id=idd, doctor="0", oy=None, day=None, soat=None)
        
        # await db.delete_user(doctor=doctor, oy=oy, day=kun, soat=soat)
        await message.answer(f"Navbat o'chirildi")
        await state.finish()
    except:
        await message.answer(f"Bu soatda mijoz yo'q")
        await state.finish()
    await db.disconnect()


@dp.message_handler(state=Band_qilish.soat)
async def fdsfdsoat(message: types.Message, state: FSMContext):
    return await message.answer(f"Noto'g'ri shakl iltimos to'g'irlab qaytadan kiriting\n"
                         f"Masalan: delet12 ")