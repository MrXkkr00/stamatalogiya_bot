# from utils.db_api.users_sql import Database_User
#
# db = Database_User(path_to_db='test.db')
#
# db.create_table_users()
# db.add_user(user_id=34123, user_name="Rasulbek", full_name="Qadomboyev_r", birth_day='11-07-2000', phone_nomer="1",
#             bonus=2, day=3, soat=4, doctor="sardor")
# user = db.select_user(user_id=34123)
# print(user)
# bonus = db.update_user_bonus(user_id=34123, bonus=22)
# print(bonus)
# day = db.update_user_qabul(user_id=34123, day=33,oy=12, soat= 12,doctor="alisher")
# print(day)
import asyncio
from time import strftime, gmtime

from utils.db_api.users_sql import Database_User


# soat = (int(strftime('%H', gmtime())) + 5) % 24
# time = str(strftime(f"%d %b {soat}:%M", gmtime()))
# oy = str(strftime(f"%B", gmtime()))
# oy_son = int(strftime(f"%m", gmtime()))
# print(time)
# print(oy)
# print(type(oy_son))
# print((oy_son))


async def test():
    db = Database_User()
    await db.create()
    # user10 = await db.select_all_users()

    # await db.drop_users()
    # await db.create_table_users()


    # print(user)
    # await db.delete_user(doctor="2", oy=2, day=31, soat=12)
    # user = await db.select_user(user_id=984568970)

    users = await db.select_all_users()
    print(users)



asyncio.run(test())

#
# soat = "10-11"
# print(soat[:2])
# print(soat[2])
# print(soat[3:5])
