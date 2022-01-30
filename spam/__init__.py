import os
from pyrogram import Client, filters
from spam.db import DB

db = DB(
    "Mongo url"
)

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

bot = Client("bot", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN)
