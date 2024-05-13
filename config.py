import os
import re
import logging
from youtube_dl import YoutubeDL
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "gofilesbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class cust(object):
    ME = None
    U_NAME = None
    B_NAME = None

class Config:
    APP_ID = int(os.environ.get("APP_ID", "7111812"))
    API_HASH = os.environ.get("API_HASH", "064880c569c803881b46d65969452ddf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6734733068:AAGQ1u7tFL5fITWmYkWMBich5gyyR0SCbII")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Music_S_eina_Bot")
    START_MSG = os.environ.get("START_MSG", "<b>Hey {}🍁,</b>\n\n<b>My Name Is</b> ᴀɴɢᴀʟɪɴᴇ <b>I am A simple Music Downloader Bot Am Only Work In Groups Just Add Me To Your Group And Use /song command</b>")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/a5a1a5ceda7dd4fb3e6de.jpg")
    HELP_MSG = os.environ.get("HELP_MSG", "👋ʜᴇy {} its very easy to request music \n\nʀᴇqᴜᴇꜱᴛ - ᴇxᴀᴍᴩʟᴇꜱ:\n<code>➲ /song Srivalli Malayalam</code>\n➲ <code>/song Darshana hridayam</code>\n➲ <code>/song Alone - Marshmallow</code>\n<code>➲ /song Aathmavile anandhame</code>\n➲ <code>/song Parayathe vannnen</code>\n\nᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟy ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴩ🍒\nʜᴏᴩᴇ yᴏᴜ ᴜɴᴅᴇʀꜱᴛᴏᴏᴅ 😌🍭")
    ABT_MSG = os.environ.get("ABT_MSG", "ʜɪ {}🍁\nɴᴀᴍᴇ:- Aɴɢᴀʟɪɴᴇ\nᴏᴡɴᴇʀ:- Rᴀɴɢᴀ 💥\nꜱᴇʀᴠᴇʀ:- Hᴇʀᴏᴋᴜ\nʙᴏᴛ ᴛyᴩᴇ:- Mᴜꜱɪᴄ Bᴏᴛ")
    GROUP_U_NAME = os.environ.get("GROUP_U_NAME", "@musiciatst")
    OWNER = os.environ.get("OWNER", " ") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
