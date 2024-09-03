import xlsxwriter
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from data.config import Doctors
from keyboards.inline.kon_loc import kontactlocatsiya, kontactlocatsiya_ru
from loader import dp
from utils.db_api.users_sql import Database_User


@dp.message_handler(text="/exel")
async def exel(message: types.Message):
    workbook = xlsxwriter.Workbook(f'data/EXEL.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "ID")
    worksheet.write('B1', "Soat")
    worksheet.write('C1', "Sana")
    worksheet.write('D1', "F.I.SH")
    worksheet.write('E1', "Doctor")
    worksheet.write('F1', "Tug'ilgan sana")
    worksheet.write('G1', "Telefon raqam")
    worksheet.write('H1', "Bonus")
    worksheet.write('I1', "Filtr uchun")

    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    son = await db_user.count_users()
    n = 2
    for i in range(1, son + 1):
        try:
            user = await db_user.select_user(id=i)
        except:
            user = [None, None, None, None, None, None, None, None, None, None]
        if not user[9] is None:
            if str(user[10]) == "1":
                doctor = "Якубов Дильшад"
            elif str(user[10]) == "2":
                doctor = "Якубов Дилмурод"
            elif str(user[10]) == "3":
                doctor = "Лор Врач"
            else:
                doctor = "None"

            filter_oy = "00" + (str(user[7]))
            filter_kun = "00" + (str(user[8]))
            filter_soat = "00" + (str(user[9]))
            sana = filter_kun[-2:] + "." + filter_oy[-2:] + ".2024"
            filter = filter_oy[-2:] + filter_kun[-2:] + filter_soat[-2:]
            worksheet.write(f'A{n}', user[0])
            worksheet.write(f'B{n}', str(user[9]) + ":00")
            worksheet.write(f'C{n}', sana)
            worksheet.write(f'D{n}', user[3])
            worksheet.write(f'E{n}', doctor)
            worksheet.write(f'F{n}', user[4])
            worksheet.write(f'G{n}', user[5])
            worksheet.write(f'H{n}', user[6])
            worksheet.write(f'I{n}', int(filter))
            n = n + 1
    await db_user.disconnect()
    workbook.close()
    await message.answer_document(InputFile(f'data/EXEL.xlsx'))
    
    
    
@dp.message_handler(text="/exelall")
async def erefrsfdsl(message: types.Message):
    workbook = xlsxwriter.Workbook(f'data/EXELALL.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "ID")
    worksheet.write('B1', "Soat")
    worksheet.write('C1', "Sana")
    worksheet.write('D1', "F.I.SH")
    worksheet.write('E1', "Doctor")
    worksheet.write('F1', "Tug'ilgan sana")
    worksheet.write('G1', "Telefon raqam")
    worksheet.write('H1', "Bonus")
    worksheet.write('I1', "Filtr uchun")

    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pass
    son = await db_user.count_users()

    n = 2
    for i in range(1, son + 1):
        try:
            user = await db_user.select_user(id=i)
        except:
            user = [None, None, None, None, None, None, None, None, None, None]
        if not user[4] is None and user[10] is None and "998" in user[5]:
            worksheet.write(f'A{n}', n-1)
            worksheet.write(f'D{n}', user[3])
            worksheet.write(f'F{n}', user[4])
            worksheet.write(f'G{n}', user[5])
            n = n + 1
    await db_user.disconnect()
    workbook.close()
    await message.answer_document(InputFile(f'data/EXELALL.xlsx'))
