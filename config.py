import os
import re
from youtube_dl import YoutubeDL

class cust(object):
    ME = None
    U_NAME = None
    B_NAME = None

class Config:
    APP_ID = int(os.environ.get("APP_ID", " "))
    API_HASH = os.environ.get("API_HASH", " ")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", " ")
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,</b>\n\n<b>My Name Is</b> 𝐌𝐈𝐎𝐍 <b>I am A simple Music Downloader Bot Am Only Work In Groups Just Add Me To Your Group And Use /song command</b>")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3357581ba3d7be61ac672.jpg")
    OWNER = os.environ.get("OWNER", " ") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
