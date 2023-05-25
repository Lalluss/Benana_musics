import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "7111812"))
    API_HASH = os.environ.get("API_HASH", "064880c569c803881b46d65969452ddf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6027561066:AAEY3zfQT3vf86UdEojodvq1rgvOmajtJZI")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "lallus_tg") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
