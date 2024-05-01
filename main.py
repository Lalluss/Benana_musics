import re
import os
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

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from aiohttp import web
from modules import web_server
PORT = environ.get("PORT", "8080")

app = web.AppRunner(await web_server())
app.setup()
bind_address = "0.0.0.0"
web.TCPSite(app, bind_address, PORT).start()

app = pyrogram.Client(
      "mlz",
       bot_token=Config.BOT_TOKEN,
       api_id=Config.APP_ID,
       api_hash=Config.API_HASH,
       plugins=dict(root="modules")
    )
app.run()
