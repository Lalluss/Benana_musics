import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "7111812"))
    API_HASH = os.environ.get("API_HASH", "064880c569c803881b46d65969452ddf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6027561066:AAEY3zfQT3vf86UdEojodvq1rgvOmajtJZI")
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,\n\n𝗠𝘆 𝗡𝗮𝗺𝗲 𝗜𝘀 Mɪᴏɴ 𝗜'𝗺 𝗔 𝗦𝗶𝗺𝗽𝗹𝗲 𝗔𝗻𝗱 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗠𝗮𝗱𝗲 𝗙𝗼𝗿 𝗠𝘂𝘀𝗶𝗰𝗦𝗲𝗶𝗻𝗮 𝗚𝗿𝗼𝘂𝗽")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/02214a2967c30c4108bc8.jpg")
    OWNER = os.environ.get("OWNER", "lallus_tg") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
