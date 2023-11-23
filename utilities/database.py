import mysql.connector as mysql
from utilities.constants import DatabaseSettings
from typing import List
from time import time
from utilities.schema import LogData

connection = mysql.connect(
    user=DatabaseSettings.USERNAME,
    password=DatabaseSettings.PASSWORD,
    host=DatabaseSettings.HOST,
    database=DatabaseSettings.DATABASE
)

class Database:
    def __init__(self):
        self.connection = connection

    def convert_to_dict(self, data: tuple) -> dict:
        return {
            "user": data[0],
            "time": data[1],
            "description": data[2],
            "id": data[3]
        } if data else {}

    def show_all(self) -> List[tuple]:
        result = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM log")
            result = [self.convert_to_dict(i) for i in cursor.fetchall()]
        return result
        
    def show_first(self, num: int) -> List[tuple]:
        result = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM log LIMIT %s", (num,))
            result = cursor.fetchall()
        return [self.convert_to_dict(i) for i in result]
    
    def insert(self, data: LogData) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT id from log ORDER BY id DESC LIMIT 1")
            previous_query = cursor.fetchone()
            last_id = previous_query[0] if previous_query else 0
            cursor.execute("INSERT INTO log VALUES (%s, %s, %s, %s)", (data.user, str(int(time())), data.description, last_id + 1))
            self.connection.commit()

    def delete(self, id: int) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM log WHERE id = %s", (id,))
            self.connection.commit()
    
    def update(self, id: int, new_data: LogData) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE log SET user = %s, time = %s, description = %s WHERE id = %s", (new_data.user, str(int(time())), new_data.description, id))
            self.connection.commit()

    def show_by_id(self, id: int) -> tuple:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM log WHERE id = %s", (id,))
            return self.convert_to_dict(cursor.fetchone())
        
    def search(self, query: str) -> List[tuple]:
        with self.connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM log WHERE description LIKE \%{query}\%")
            return [self.convert_to_dict(i) for i in cursor.fetchall()]
        
    def clear(self):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM log")
            self.connection.commit()
        