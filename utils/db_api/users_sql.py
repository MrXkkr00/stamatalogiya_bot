from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from numpy import double
from sqlalchemy import BIGINT

from data import config


class Database_User:

    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None

    async def create(self):
        try:
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
        except Exception as e:
            print(f"Error creating connection pool: {e}")

    async def disconnect(self):
        try:
            await self.pool.close()
        except Exception as e:
            print(f"Error closing connection pool: {e}")

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_id varchar(255),
            user_name varchar(255),
            full_name varchar(255),
            birth_day varchar(255),
            phone_nomer varchar(255),
            bonus int,
            oy int,
            day int,
            soat int,
            doctor varchar(255)
            );
"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id: str = None, user_name: str = None, full_name: str = None,
                       birth_day: str = None, phone_nomer: str = None, bonus: int = None, oy: int = None,
                       day: int = None, soat: int = None, doctor: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, user_name, full_name, birth_day, phone_nomer, bonus, oy, day, soat, doctor) 
        VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10) returning *
        """
        return await self.execute(sql, user_id, user_name, full_name, birth_day, phone_nomer, bonus, oy, day, soat,
                                  doctor, fetchrow=True)

    async def update_user_bonus(self, phone_nomer, bonus):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET bonus=$1 WHERE phone_nomer=$2
        """
        return await self.execute(sql, bonus, phone_nomer, fetchrow=True)

    async def update_user_qabul(self, user_id, doctor, oy, day, soat):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET doctor=$1, oy = $2,day=$3, soat=$4 WHERE user_id=$5
        """
        return await self.execute(sql, doctor, oy, day, soat, user_id, fetchrow=True)

    async def update_id(self, id, doctor, oy, day, soat):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET doctor=$1, oy = $2,day=$3, soat=$4 WHERE id=$5
        """
        return await self.execute(sql, doctor, oy, day, soat, id, fetchrow=True)

    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        return await self.execute("SELECT COUNT(*) FROM Users", fetchval=True)

    async def delete_user(self, doctor, oy, day, soat):
        await self.execute("DELETE FROM Users WHERE doctor=$1 AND oy = $2 AND day=$3 AND soat =$4 ", doctor, oy, day,
                           soat, execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
