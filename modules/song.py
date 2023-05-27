from pyrogram import Client, filters

import yt_dlp
from youtube_search import YoutubeSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import ChatWriteForbidden

ABS="Sᴜᴘᴘᴏʀᴛ"
APPER="lallus"
OWNER="Owner"
GITCLONE="github.com/shamilhabeebnelli/song-bot"
B2="telegram.dog/edit_repo"
BUTTON1="🌿 Gʀᴏᴜᴘ"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(BUTTON1, url=f"https://t.me/+BzleUoO-duFmODRl")
                ]
            ]
         ),
    )


@Client.on_message(filters.command(['song']) & filters.group)
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 7000:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[@AnnabenbotZ]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            message.reply_text('**👎 Nothing found Retry with another !**')
            return
    except Exception as e:
        message.reply_text(
            "**Enter Song Name with /song Command!**"
        )
        print(str(e))
        return
    m=message.reply_text("<code>✨ Fetching... </code>")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep =f'<a>{title}</a>\n\n❍ <b>Duration:</b> <code>{duration}</code>\n❍ <b>Uploaded By:</b> <a href="https://t.me/Edit_Repo">BenbotZ</a>\n<b>❍ Source:</b> <a href="{link}">Click Here</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                  InlineKeyboardButton("send personaly", url=f'https://t.me/Annasong_bot?start=audio_file')
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )
        m.delete()
    except Exception as e:
        m.edit('**An internal Error Occured, Report This @Edit_repo !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
@Client.on_message(filters.regex(r'(https?://)?.*you[^\s]+'))
def ytsng(client, message):

    downurl=message.matches[0].group(0)

    url =".join(message.command[1:])"
    query =".join(message.command[1:])"
    m=message = message.reply("<code>✨ Fetching... </code>")
    
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(downurl, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            performer = f"[@AnnabenbotZ]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**👎 Nothing found Retry with another !**')
            return
    except Exception as e:
        m.edit(
            "**Enter Song Name with /song Command!**"
        )
        print(str(e))
        return
    m.edit("`Uploading...🍁`")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep =f'<a>{title}</a>\n\n❍ <b>Duration:</b> <code>{duration}</code>\n❍ <b>Uploaded By:</b> <a href="https://t.me/Edit_Repo">BenbotZ</a>\n<b>❍ Source:</b> <a href="{link}">Click Here</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                  InlineKeyboardButton("send personaly", callback_data=f"sendpm")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )
        m.delete()
    except Exception as e:
        m.edit('**An internal Error Occured, Report This @Edit_repo !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)     
        
