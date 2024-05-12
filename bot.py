import os

from pyrogram import Client
from user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None
