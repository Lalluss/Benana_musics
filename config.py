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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6383975910:AAGCu6AKfrBc8Ptyqi22KW3ZQr8mBhhNpNA")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Music_S_eina_bot")
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,</b>\n\n<b>My Name Is</b> ѦηηѦ ɓ℮η <b>I am A simple Music Downloader Bot Am Only Work In Groups Just Add Me To Your Group And Use /song command</b>")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/4ba4a9a9a5d26a33fe435.jpg")
    OWNER = os.environ.get("OWNER", " ") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
