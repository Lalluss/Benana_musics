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
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,</b>\n\n<b>My Name Is</b> ᴀɴɢᴀʟɪɴᴇ <b>I am A simple Music Downloader Bot Am Only Work In Groups Just Add Me To Your Group And Use /song command</b>")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/a5a1a5ceda7dd4fb3e6de.jpg")
    HELP_MSG = os.environ.get("HELP_MSG", "👋ʜᴇy its very easy to request music here\n\nʀᴇqᴜᴇꜱᴛ - ᴇxᴀᴍᴩʟᴇꜱ:\n<code>➲ /song Srivalli Malayalam</code>\n➲ <code>/song Darshana hridayam</code>\n➲ <code>/song Alone - Marshmallow</code>\n<code>➲ /song Aathmavile anandhame</code>\n➲ <code>/song Parayathe vannnen</code>\n\nʜᴏᴩᴇ yᴏᴜ ᴜɴᴅᴇʀꜱᴛᴏᴏᴅ 😌🍭')")
    OWNER = os.environ.get("OWNER", " ") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
