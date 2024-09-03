from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.Keyboards import bosh_menu, contact_keyboard, bosh_menu_ru
from loader import dp
from utils.db_api.users_sql import Database_User


class Qabul_State_ru(StatesGroup):
    ism = State()
    familya = State()
    birth_day = State()
    contact = State()


class Yozilish_ru_ru(StatesGroup):
    doctor = State()
    day = State()
    soat = State()


@dp.message_handler(state=Qabul_State_ru.ism)
async def qabul21_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Введите свою фамилию : ")
    await Qabul_State_ru.next()


@dp.message_handler(state=Qabul_State_ru.familya)
async def qabul2_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"familya": message.text}
    )

    await message.answer(f"Введите вашу дату рождения : \n"
                         f"Например (день.месяц.год):  11.07.2000", reply_markup=ReplyKeyboardRemove())
    await Qabul_State_ru.next()


@dp.message_handler(lambda message: len(message.text) == 10 and message.text[0:2].isdigit()
                                    and message.text[3:5].isdigit() and message.text[6:10].isdigit(),
                    state=Qabul_State_ru.birth_day)
async def qabul13_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"birthday": str(message.text)}
    )
    await message.answer(f"Отправьте свой контакт : ", reply_markup=contact_keyboard)
    await Qabul_State_ru.next()


@dp.message_handler(state=Qabul_State_ru.birth_day)
async def qabu1l3_ru(message: types.Message, state: FSMContext):
    return await message.answer(f"Неверная форма, исправьте и отправьте повторно.\n"
                                f"Например (день.месяц.год):  01.07.2000\n03,12,1995\n23 06 1987")


@dp.message_handler(content_types="contact", state=Qabul_State_ru.contact)
async def qabul3_ru(message: types.Message, state: FSMContext):
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
    await message.answer(f"{fullname}\n{phone_number}\n{birth_day}\nВы зарегистрированы : ", reply_markup=bosh_menu_ru)
    await db_user.disconnect()
    await state.finish()
