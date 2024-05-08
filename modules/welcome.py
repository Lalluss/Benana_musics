#creatod by @Am_lallu_tg
from pyrogram import Client , filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import os
import random
from random import choice

import math
from PIL import Image, ImageDraw, ImageFont


@client.on_message(filters.new_chat_members)
async def new(_, m: Message):
    if m.from_user.id:
        chat = m.chat.title 
        senko = Image.open('senko.gif')
        senkos = [senko.copy()]

        try:
            while 1:
                senko.seek(senko.tell() + 4)
                owo = senko.copy()
                senkos.append(owo)

        except EOFError:
            pass

        senkos[0] = senkos[0]

        senkotext = [f'Welcome to the {m.chat.username}! master {m.from_user.first_name}']

        s1 = senkos[0].size[0] // 2
        s2 = 240    
        senkofont = ImageFont.truetype("fonts.otf", 15)
        s3 = math.ceil(len(senkos) / len(senkotext))

        for i in range(len(senkos)):
            draw = ImageDraw.Draw(senkos[i])
            s4 = (s1 - len(senkotext[i // s3]) * 4, s2)
            draw.text(s4, senkotext[i // s3], font=senkofont, anchor=None)

        senkos[0].save("newsenko.gif",
                     save_all=True,
                     append_images=senkos[1:],
                     optimize=False, 
                     duration=150,              
                     loop=0)

        await m.reply_video(video="newsenko.gif", caption=f"Welcome to the {m.chat.username}! master {m.from_user.first_name}")
  
senko_group = 6
 
@client.on_message(
    filters.group
    & filters.incoming
    & filters.reply
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=senko_group,
)
async def senko(_, message):
    getme = await bot.get_me()
    id = getme.id
    if not message.reply_to_message.from_user.id == id:
        return
    RANDOM = (
        "yes {message.from_user.mention}",
        "uwu understand! u~u *does not really understand*",
        "Hmm... :c",
        "you are funny",
        "hahhahaha ;",
        "k",
        "who",
    )
    await message.reply_text(choice(RANDOM))

