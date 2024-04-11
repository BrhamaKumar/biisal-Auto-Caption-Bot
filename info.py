# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6301693754"))
API_ID = int(getenv("API_ID", "20810825"))
API_HASH = str(getenv("API_HASH", "707e67f53b4593a3e9b6b424311f84d0"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "6737613081:AAGwZd1WYOBEoPSg9BjzHhiDHpaH64a7A8g"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://daniel811802:0wQNzmwMkUiqOZa1@cluster0.8jaksiw.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/bisal_files'>{file_name} Telegram : @Bisal_Files\n\nForward the file before Downloading.</a></b>",
    )
)
