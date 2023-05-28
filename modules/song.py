from pyrogram import Client, filters

import yt_dlp
from youtube_search import YoutubeSearch
import requests
import wget

import os
import time
import hashlib 
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import ChatWriteForbidden

ABS="Sᴜᴘᴘᴏʀᴛ"
APPER="lallus"
OWNER="Owner"
GITCLONE="github.com/shamilhabeebnelli/song-bot"
B2="telegram.dog/edit_repo"
BUTTON1="🍃 Gʀᴏᴜᴘ"
AUDIO = {}

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
async def song_fetch(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count > 0:
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
            hash_object = hashlib.sha256()
            hash_object.update(title.encode('utf-8'))
            hash_value = hash_object.hexdigest()
            keyw = hash_value[:5]

        except Exception as e:
            print(e)
            await message.reply_text('**👎 Nothing found Retry with another !**')
            return
    except Exception as e:
        await message.reply_text(
            "**Enter Song Name with /song Command!**"
        )
        print(str(e))
        return
    m = await message.reply_text("<code>✨ Fetching... </code>")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            AUDIO[keyw] = {
                "audio_file": audio_file,
                "title": title,
                "duration": duration,
                "link": link,
                "thumb_name": thumb_name
            }
        rep = f'<a>{title}</a>\n\n❍ <b>Duration:</b> <code>{duration}</code>\n❍ <b>Uploaded By:</b> <a href="https://t.me/Edit_Repo">BenbotZ</a>\n<b>❍ Source:</b> <a href="{link}">Click Here</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await message.reply_audio(
            audio_file, caption=rep, parse_mode='HTML', quote=False, title=title, duration=dur, performer=performer,
            thumb=thumb_name,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✨ Send - Personally ✨", callback_data=f'sendpm#{keyw}')
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
        await m.delete()
    except Exception as e:
        await message.reply_text('**An internal Error Occured, Report This @Edit_repo !!**')
        print(e)
    


@Client.on_message(filters.regex(r'(https?://)?.*you[^\s]+'))
async def ytsng(client, message):
    downurl = message.matches[0].group(0)

    url = ".join(message.command[1:])"
    query = ".join(message.command[1:])"

    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count > 0:
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
            hash_object = hashlib.sha256()
            hash_object.update(title.encode('utf-8'))
            hash_value = hash_object.hexdigest()
            keyw = hash_value[:5]

        except Exception as e:
            print(e)
            await message.reply_text('**👎 Nothing found Retry with another !**')
            return
    except Exception as e:
        await m.edit(
            "**Enter Song Name with /song Command!**"
        )
        print(str(e))
        return
    d=await message.reply_text("`✨ Fetching... `")
    h = None  # Assign a default value to 'h'
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            AUDIO[keyw] = {
                "audio_file": audio_file,
                "title": title,
                "duration": duration,
                "link": link,
                "thumb_name": thumb_name
            }
        rep = f'<a>{title}</a>\n\n❍ <b>Duration:</b> <code>{duration}</code>\n❍ <b>Uploaded By:</b> <a href="https://t.me/Edit_Repo">BenbotZ</a>\n<b>❍ Source:</b> <a href="{link}">Click Here</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        h = await message.reply_audio(
            audio_file, caption=rep, parse_mode='HTML', quote=False, title=title, duration=dur, performer=performer,
            thumb=thumb_name,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✨ Send - Personally ✨", callback_data=f"sendpm#{keyw}")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
        await d.delete()
    except Exception as e:
        await message.reply_text('**An internal Error Occured, Report This @Edit_repo !!**')
        print(e)
    try:
        await os.remove(audio_file)
        await os.remove(thumb_name)
    except Exception as e:
        print(e)   

         
@Client.on_message(filters.command('find') & filters.text)
async def song(client, message):
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/find requires an argument.")
    if args.startswith(" "):
        await message.reply("/find requires an argument.")
        return
    m= await message.reply("`Wait Am Finding Ur Song...`")

    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await message.reply(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    duration = r['data']['results'][0]["duration"]
    performer = f"[@AnnabenbotZ]"
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    hash_object = hashlib.sha256()
    hash_object.update(sname.encode('utf-8'))
    hash_value = hash_object.hexdigest()
    keyw = hash_value[:5]
    
    cap = f'<a>{sname}</a>\n\n❍ <b>Duration:</b> <code>{duration}</code>\n❍ <b>Uploaded By:</b> <a href="https://t.me/Edit_Repo">BenbotZ</a>\n<b>❍ Source:</b> <a href="{slink}">Click Here</a>'
    
    r[keyw] = {
    "audio_file": file,
    "title": sname,
    "duration": duration,
    "link": slink,
    "thumb_name": thumbnail
    }
    await m.edit("`✨ Fetching...`")
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=cap,thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(
           [
              [
                 InlineKeyboardButton("✨ Send - Personally ✨", callback_data=f"sendpm#{keyw}")
              ]
           ]
        ),
    )
    os.remove(ffile)
    os.remove(thumbnail)
    await m.delete()
    
@Client.on_callback_query(filters.regex(r"^sendpm"))
async def callback_handler(client, query):
    data = query.data
    sng = data.split("#")[1]
    audio_file = AUDIO[sng]["audio_file"]  
    duration = AUDIO[sng]["duration"]
    title = AUDIO[sng]["title"]    
    link = AUDIO[sng]["link"]
    performer = f"[@AnnabenbotZ]"
    thumb_name = AUDIO[sng]["thumb_name"]
    rep = f'<a>{title}</a>\n\n❍ <b>Duration:</b> <code>{duration}</code>\n❍ <b>Uploaded By:</b> <a href="https://t.me/Edit_Repo">BenbotZ</a>\n<b>❍ Source:</b> <a href="{link}">Click Here</a>'  
    try:
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        user_id = query.from_user.id        
        await client.send_audio(user_id, audio_file, caption=rep, parse_mode='HTML', title=title, duration=dur, performer=performer, thumb=thumb_name, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ɢʀᴏᴜᴘ ✨🌟", url="https://t.me/+BzleUoO-duFmODRl")]]))
        await query.answer("Audio Send Successfully", show_alert=True)
    except ChatWriteForbidden:
        print("Cannot send a message to this user.")     
        await query.answer("Start The Bot!", show_alert=True)
