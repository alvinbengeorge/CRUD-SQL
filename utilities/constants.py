from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseSettings:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    DATABASE = os.getenv("DATABASE")