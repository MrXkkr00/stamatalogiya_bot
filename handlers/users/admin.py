from data.config import Doctors, ADMINS
from keyboards.default.Keyboards import admin_menu, admin_admin, bosh_menu
from loader import bot

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.qabul_uchun import kun, Yakubov_Dilmurod_ru, \
    Yakubov_Dilshod_ru, Lor_ru, oy
from loader import dp
from utils.db_api.users_sql import Database_User

class BonusState(StatesGroup):
    raqam = State()
    bonus = State()



class Qabul_admin(StatesGroup):
    doctor = State()
    oy = State()
    kun = State()


@dp.message_handler(text="/admin", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]])
async def kontact(message: types.Message):
    await message.answer(f"Admin", reply_markup=admin_menu)


@dp.message_handler(text="/admin", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]] , state=[BonusState.bonus, BonusState.raqam])
async def k1321ontact(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=admin_menu)
    await state.finish()


@dp.message_handler(text="/admin", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]],  state=[Qabul_admin.doctor, Qabul_admin.oy, Qabul_admin.kun])
async def konta1231ct(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=admin_menu)
    await state.finish()



@dp.message_handler(text="/start",  state=[BonusState.bonus, BonusState.raqam])
async def kon2421tact(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="/start",  state=[Qabul_admin.doctor, Qabul_admin.oy, Qabul_admin.kun])
async def kon4124tact(message: types.Message, state: FSMContext):
    await message.answer(f"Admin", reply_markup=bosh_menu)
    await state.finish()








@dp.message_handler(text="/admin", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]])
async def kontact(message: types.Message):
    await message.answer(f"Admin", reply_markup=admin_menu)







@dp.message_handler(text="/navbat", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]])
async def qabul1_ru(message: types.Message):
    await message.answer(f"Выберите врача : ", reply_markup=admin_admin)
    await message.answer_photo(photo=InputFile("./data/rasm/dilshod.jpg"), reply_markup=Yakubov_Dilshod_ru)
    await message.answer_photo(photo=InputFile("./data/rasm/dilmurod.jpg"), reply_markup=Yakubov_Dilmurod_ru)
    await message.answer_photo(photo=InputFile("./data/rasm/lor.jpg"), reply_markup=Lor_ru)
    await Qabul_admin.doctor.set()


# @dp.message_handler(text="/navbat", state=[Qabul_admin.doctor, Qabul_admin.oy, Qabul_admin.kun])
# async def qabul1_ru(message: types.Message):
#     await message.answer(f"Выберите врача : ", reply_markup=admin_admin)
#     await message.answer_photo(photo=InputFile("./data/rasm/dilshod.jpg"), reply_markup=Yakubov_Dilshod_ru)
#     await message.answer_photo(photo=InputFile("./data/rasm/dilmurod.jpg"), reply_markup=Yakubov_Dilmurod_ru)
#     await message.answer_photo(photo=InputFile("./data/rasm/lor.jpg"), reply_markup=Lor_ru)
#     await Qabul_admin.doctor.set()


@dp.callback_query_handler(text_contains="#", state=Qabul_admin.doctor)
async def location_ru(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"doctor": call.data[1:2]}
    )
    await call.message.answer(f"Нажмите на нужный месяц", reply_markup=admin_admin)
    await call.message.answer(f"Выберите месяц", reply_markup=oy)
    await Qabul_admin.oy.set()


@dp.callback_query_handler(text_contains="0000", state=Qabul_admin.oy)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    oy1 = int(int(callback_data) / 10000)
    await state.update_data(
        {"oy": oy1}
    )
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Выберите день", reply_markup=kun)
    await Qabul_admin.next()


@dp.callback_query_handler(text_contains="99", state=Qabul_admin.kun)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    kun1 = int(int(callback_data) / 100)
    await state.update_data(
        {"kun": kun1}
    )
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
                                  f"☎️Number : {user[5]}")
    if user11:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=11, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")
    if user12:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=12, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")
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
                                  f"☎️Number : {user[5]}")
    if user15:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=15, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")
    if user16:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=16, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")
    if user17:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=17, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")
    if user18:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=18, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")

    if user24:
        test = 1
        user = await db_user.select_user(oy=oy, day=kun, soat=24, doctor=doctor)
        doctor_number = int(user[10])
        await call.message.answer(f"📝{user[9]}:00  {user[8]}.{user[7]}  \n"
                                  f"👨‍⚕️Doctor : {Doctors[doctor_number]}\n"
                                  f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                  f"👼Tug'ilgan sana : {user[4]}\n"
                                  f"☎️Number : {user[5]}")
    if test == 0:
        await call.message.answer(f"Сегодня никого нет.", reply_markup=admin_menu)
    await db_user.disconnect()
    await state.finish()





























    
    
import json
from time import strftime, gmtime
    
@dp.message_handler(text = "/delete", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]])
async def delet(massage:types.Message):
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    son = await db_user.count_users()
    for i in range(1, son+1):
        try:
        
            user = await db_user.select_user(id=i)
            # print(user)
            oy_asl = int(strftime(f"%m", gmtime()))
            kun_asl= int(strftime(f"%d", gmtime()))
            kun=int(user[8])
            oy = int(user[7])
            # print(oy_asl)
            # print(oy)
            # print(kun_asl)
            # print(kun)
            
            if oy == oy_asl:
                if kun < kun_asl:
                    await db_user.update_id(id=i, oy=None, day=None, soat=None, doctor=None)
                        
            if oy < oy_asl:
                await db_user.update_id(id=i, oy=None, day=None, soat=None, doctor=None)
            # user = await db_user.select_user(id=i)
            # print(user)
        except:
            pass
    
    
    
    
    
    
    
    
    
    
    
    
    
