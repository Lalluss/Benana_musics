import os
import re
from youtube_dl import YoutubeDL

class cust(object):
    ME = None
    U_NAME = None
    B_NAME = None

class Config:
    APP_ID = int(os.environ.get("APP_ID", "7111812"))
    API_HASH = os.environ.get("API_HASH", "064880c569c803881b46d65969452ddf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6985438359:AAGkbDefY73myVSMMY5zK15YEPOxVF-wepU")
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,</b>\n\n<b>My Name Is</b> 𝐌𝐈𝐎𝐍 <b>I am A simple Music Downloader Bot Am Only Work In Groups Just Add Me To Your Group And Use /song command</b>")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/895e4c2ad6766acabedb1.jpg")
    OWNER = os.environ.get("OWNER", " ") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
