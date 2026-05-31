import os
from pyrogram import Client
from config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Lallus(Client):
    def __init__(self):
        super().__init__(
            name=Config.SESSION,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=50,
            plugins={"root": "modules"},
            sleep_threshold=5,
        )

bot = Lallus()
bot.run()
