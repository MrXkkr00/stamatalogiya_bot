from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.Keyboards import bosh_menu, contact_keyboard
from loader import dp
from utils.db_api.users_sql import Database_User


class Qabul_State(StatesGroup):
    ism = State()
    familya = State()
    birth_day = State()
    contact = State()


@dp.message_handler(state=Qabul_State.ism)
async def qabul2(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Familyangizni kiriting : ")
    await Qabul_State.next()


@dp.message_handler(state=Qabul_State.familya)
async def qabul2(message: types.Message, state: FSMContext):
    await state.update_data(
        {"familya": message.text}
    )
    await message.answer(f"Tug'ulgan kunizni kiriting : \n"
                         f"Masalan (kun.oy.yil):  11.07.2000", reply_markup=ReplyKeyboardRemove())
    await Qabul_State.birth_day.set()


@dp.message_handler(lambda message: len(message.text) == 10 and message.text[0:2].isdigit()
                                    and message.text[3:5].isdigit() and message.text[6:10].isdigit(),
                    state=Qabul_State.birth_day)
async def qabul13(message: types.Message, state: FSMContext):
    await state.update_data(
        {"birthday": str(message.text)}
    )
    await message.answer(f"Kontaktizni yuboring : ", reply_markup=contact_keyboard)
    await Qabul_State.contact.set()


@dp.message_handler(state=Qabul_State.birth_day)
async def qabu1l3(message: types.Message, state: FSMContext):
    return await message.answer(f"noto'g'ri shakl, to'g'irlab qaytadan yuboring\n"
                                f"Masalan (kun.oy.yil):  11.07.2000\n03,12,1995\n23 06 1987")


@dp.message_handler(content_types="contact", state=Qabul_State.contact)
async def qabul3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = (str(message.from_user.id))
    user_name = message.from_user.username
    fullname = data.get("ism") + " "
    fullname += data.get("familya")
    phone_number = message.contact.phone_number
    birth_day = data.get("birthday")
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    try:
        await db_user.create_table_users()
    except:
        pass
    await db_user.add_user(user_id=user_id, user_name=user_name, full_name=fullname, phone_nomer=phone_number,
                           birth_day=birth_day)
    await message.answer(f"{fullname}\n{phone_number}\n{birth_day}\nSiz ro'yxatga olindingiz: ",
                         reply_markup=bosh_menu)
    await db_user.disconnect()

    await state.finish()
