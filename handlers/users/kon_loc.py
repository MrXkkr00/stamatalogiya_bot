from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.kon_loc import kontactlocatsiya, kontactlocatsiya_ru
from loader import dp


@dp.message_handler(text="📲️Kontaktlar")
async def kontact(message: types.Message):
    await message.answer(f"Telephone \n+998712958020", reply_markup=kontactlocatsiya)


@dp.message_handler(text="📍Lokatsiya")
async def location(message: types.Message):
    await message.answer("https://yandex.ru/maps/org/224000326082")


@dp.message_handler(text="📲️Контакты")
async def kontact_ru(message: types.Message):
    await message.answer(f"Телефон \n+998712958020", reply_markup=kontactlocatsiya_ru)


@dp.message_handler(text="📍Локация")
async def location_ru(message: types.Message):
    await message.answer("https://yandex.ru/maps/org/224000326082")





