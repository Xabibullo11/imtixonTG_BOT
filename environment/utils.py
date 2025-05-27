from os import getenv

from dotenv import load_dotenv

load_dotenv()

class Bot:
    TOKEN = getenv("TOKEN")
    DB_URL = getenv("DB_URL")


class Env:
    bot = Bot()