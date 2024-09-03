from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.kon_loc import kontactlocatsiya
from loader import dp
from utils.db_api.users_sql import Database_User
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


@dp.message_handler(text="💵Bonuslarim")
async def bonus(message: types.Message):
    user_id = str(message.from_user.id)
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass

    user = await db_user.select_user(user_id=str(user_id))
    if user[6]:
        await message.answer(f"Sizning bonusingiz \n💵{user[6]} so'm")
    else:
        await message.answer(f"Sizda hali bonuslar mavjud emas")
    await db_user.disconnect()


@dp.message_handler(text="💵Мои бонусы")
async def bonus(message: types.Message):
    user_id = str(message.from_user.id)
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    user = await db_user.select_user(user_id=str(user_id))
    if user[6]:
        await message.answer(f"Ваш бонус \n💵{user[6]} сум")
    else:
        await message.answer(f"У вас еще нет бонусов")
    await db_user.disconnect()


@dp.message_handler(text="/bonus", user_id=[ADMINS[0], ADMINS[1], ADMINS[2], ADMINS[3]])
async def bonus_ad123213min(message: types.Message):
    await message.answer(f"Foydalanuvchi raqamini yuboring\n"
                         f"Masalan: 991112233", reply_markup=admin_admin)
    await BonusState.raqam.set()


@dp.message_handler(lambda message: len(message.text) == 9 and message.text.isdigit(), state=BonusState.raqam)
async def bonus_ra32qam(message: types.Message, state: FSMContext):
    nomer = "998" + str(message.text)
    nomer_1 = "+998" + str(message.text)
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pas = 1

    user = await db_user.select_user(phone_nomer=nomer)
    user_1 = await db_user.select_user(phone_nomer=nomer_1)

    print(user)
    print(user_1)
    test = 0

    try:
        if not user is None:
            text = 1
            test = 1
            await state.update_data(
                {"nomer": "998" + str(message.text)}
            )
            await message.answer(text=f"🙎🏻‍♂️Mijoz : {user[3]}\n"
                                      f"👼Tug'ilgan sana : {user[4]}\n"
                                      f"☎️Number : +{user[5]}\n"
                                      f"bonus : {user[6]}")
            await message.answer(f"Bonus miqdorini yuboring so'mda va faqat raqamda : \n"
                                 f"Masalan: 50000")
    except:
        pas = 1

    try:
        if not user_1 is None:
            test = 1
            await state.update_data(
                {"nomer": ("+998" + str(message.text))}
            )
            await message.answer(text=f"🙎🏻‍♂️Mijoz : {user_1[3]}\n"
                                      f"👼Tug'ilgan sana : {user_1[4]}\n"
                                      f"☎️Number : +{user_1[5]}\n"
                                      f"bonus : {user_1[6]}")
            await message.answer(f"Bonus miqdorini yuboring so'mda va faqat raqamda : \n"
                                 f"Masalan: 50000")
    except:
        pas = 1

    await db_user.disconnect()

    if test == 0:
        await message.answer(f"Bu raqam egasi topilmadi\n"
                             f"Iltimos raqamni tekshirib qaytadan kiriting", reply_markup=admin_admin)
        await state.finish()

    if test == 1:
        await BonusState.bonus.set()
    await db_user.disconnect()


@dp.message_handler(state=BonusState.raqam)
async def bon565us_r(message: types.Message):
    return await message.answer(f"Noto'g'ti shakl iltimos to'g'ri yuboring:"
                                f"\n952221133\n"
                                f"971113322", reply_markup=admin_admin)


@dp.message_handler(lambda message: not message.text.isdigit(), state=BonusState.bonus)
async def bonus_rsumm(message: types.Message):
    return await message.answer(f"Faqat raqam kiriting", reply_markup=admin_admin)


@dp.message_handler(lambda message: message.text.isdigit(), state=BonusState.bonus)
async def bonus_sum(message: types.Message, state: FSMContext):
    bonus = int(message.text)
    data = await state.get_data()
    nomer = str(data.get("nomer"))
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    try:
        await db_user.update_user_bonus(phone_nomer=nomer, bonus=bonus)
        await message.answer(f"Bonus qabul qilindi", reply_markup=admin_admin)
    except:
        await message.answer(f"Iltimos bonusni qaytadan kiriting", reply_markup=admin_menu)
    await db_user.disconnect()
    await state.finish()
