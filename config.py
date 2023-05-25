import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "7111812"))
    API_HASH = os.environ.get("API_HASH", "064880c569c803881b46d65969452ddf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6027561066:AAEY3zfQT3vf86UdEojodvq1rgvOmajtJZI")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Song Downloader I am only Work MusicSiena Group Click The Group Btn And join group and ask songs with command there\n\n/song - song name")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3ca56321b6b3ccaa84929.jpg")
    OWNER = os.environ.get("OWNER", "lallus_tg") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
