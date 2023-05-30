import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "8549422"))
    API_HASH = os.environ.get("API_HASH", "1cb02e0eb2c67d504e77c1bd268399ae)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6027561066:AAEY3zfQT3vf86UdEojodvq1rgvOmajtJZI")
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,\n\n𝗠𝘆 𝗡𝗮𝗺𝗲 𝗜𝘀 Mɪᴏɴ 𝗜'𝗺 𝗔 𝗦𝗶𝗺𝗽𝗹𝗲 𝗔𝗻𝗱 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗠𝗮𝗱𝗲 𝗙𝗼𝗿 MᴜsɪᴄSᴇɪɴᴀ Gʀᴏᴜᴘ")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/02214a2967c30c4108bc8.jpg")
    OWNER = os.environ.get("OWNER", "lallus_tg") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
