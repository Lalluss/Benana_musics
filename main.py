import pyrogram
import re
from os import environ

from pyrogram.raw.all import layer

from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
from config import Config

logging.getLogger("pyrogram").setLevel(logging.WARNING)


from aiohttp import web
from Lallus import web_server
PORT = environ.get("PORT", 8080)

app = Client("SESSION",
api_id=Config.APP_ID, 
api_hash=Config.API_HASH, 
bot_token=Config.BOT_TOKEN)

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
    async def start(self):
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

bot = Lallus()
bot.run()
