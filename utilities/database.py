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

    def show_all(self) -> List[tuple]:
        result = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM log")
            result = cursor.fetchall()
        return result
        
    def show_first(self, num: int) -> List[tuple]:
        result = []
        with self.connection.cursor as cursor:
            cursor.execute("SELECT * FROM log LIMIT %s", (num,))
            result = cursor.fetchall()
        return result
    
    def insert(self, data: LogData) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO log VALUES (%s, %s, %s)", (data.user, str(int(time())), data.description))
            self.connection.commit()
        