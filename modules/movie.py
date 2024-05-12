import re
import os
import time

from bot import Bot
from presets import Presets
from base64 import b64encode
from init import user_message
from utils.file_size import get_size
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

if os.environ.get("ENV", False):
    from sample_config import Config
else:
    from config import Config
    
ASK_PM_TEXT = "<b>Click the below button</b>"

BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
PM_ERROR = "<b>Unable to send medias</b> ⛔️\n<code>Click the below button\nAsk here for movies later!</code>"
MEDIA_SEND_TEXT = "<code>Media dispatched as PM 🥳</code>"
NO_MEDIA = "Requested movie: <b>{}</b>\n\n<b>Not available " \
           "Right Now</b>\n<code>Possible Causes : 🤔\n\n⭕️ Not " \
           "released yet</code>\n⭕️ <a href='https://www.google.com/search?q={}'> Spelled incorrectly</a>\n" \
           "<code>⭕️ Unwanted texts in Msgs\n⭕ Asking theatre prints\n⭕ Not in ma Database</code>"

@Client.on_message(filters.group & filters.text)
async def query_mgs(client: Bot, message: Message):
    query_message = message.text
    block_list = BLOCK_LIST
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if query_message.startswith(tuple(block_list)):
        return
    info = await client.get_me()
    user_message.clear()
    if len(message.text) > 2:
        try:
            for channel in Config.CHANNELS:
                # Looking for Document type in messages
                async for messages in client.USER.search_messages(channel, query_message, filter="document", limit=50):
                    doc_file_names = messages.document.file_name
                    file_size = get_size(messages.document.file_size)
                    if re.compile(rf'{doc_file_names}', re.IGNORECASE):
                        try:
                            await client.send_chat_action(
                                chat_id=message.from_user.id,
                                action="upload_document"
                            )
                        except Exception:
                            query_bytes = query_message.encode("ascii")
                            base64_bytes = b64encode(query_bytes)
                            secret_query = base64_bytes.decode("ascii")
                            await client.send_message(
                                chat_id=message.chat.id,
                                text=ASK_PM_TEXT,
                                reply_to_message_id=message.message_id,
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton(
                                            "👉 CLICK HERE 👈", url="t.me/{}?start={}".format(info.username, secret_query))
                                         ]
                                    ])
                            )
                            return
                        media_name = messages.document.file_name.rsplit('.', 1)[0]
                        media_format = messages.document.file_name.split('.')[-1]
                        try:
                            await client.copy_message(
                                chat_id=message.from_user.id,
                                from_chat_id=messages.chat.id,
                                message_id=messages.message_id,
                                caption=Config.GROUP_U_NAME+CAPTION_TEXT_DOC.format(media_name,
                                                                                            media_format, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(e.x)
                        user_message[id] = message.message_id
                # Looking for video type in messages
                async for messages in client.USER.search_messages(channel, query_message, filter="video", limit=50):
                    vid_file_names = messages.caption
                    file_size = get_size(messages.video.file_size)
                    if re.compile(rf'{vid_file_names}', re.IGNORECASE):
                        try:
                            await client.send_chat_action(
                                chat_id=message.from_user.id,
                                action="upload_video"
                            )
                        except Exception:
                            query_bytes = query_message.encode("ascii")
                            base64_bytes = b64encode(query_bytes)
                            secret_query = base64_bytes.decode("ascii")
                            await client.send_message(
                                chat_id=message.chat.id,
                                text=ASK_PM_TEXT,
                                reply_to_message_id=message.message_id,
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton(
                                            "👉 CLICK HERE 👈", url="t.me/{}?start={}".format(info.username, secret_query))
                                         ]
                                    ])
                            )
                            return
                        media_name = message.text.upper()
                        try:
                            await client.copy_message(
                                chat_id=message.from_user.id,
                                from_chat_id=messages.chat.id,
                                message_id=messages.message_id,
                                caption=Config.GROUP_U_NAME+CAPTION_TEXT_VID.format(media_name, file_size)
                            )
                        except FloodWait as e:
                            time.sleep(e.x)
                        user_message[id] = message.message_id
        except Exception:
            try:
                await client.send_message(
                    chat_id=message.chat.id,
                    text=PM_ERROR,
                    reply_to_message_id=message.message_id,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(
                                "👉 START BOT 👈", url="t.me/{}".format(info.username))
                             ]
                        ])
                )
            except Exception:
                pass
            return
        if user_message.keys():
            try:
                await client.send_message(
                    chat_id=message.chat.id,
                    text=MEDIA_SEND_TEXT,
                    reply_to_message_id=user_message[id],
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(
                                "👉 Click Here To View 👈", url="t.me/{}".format(info.username))
                             ]
                        ])
                )
                user_message.clear()
            except Exception:
                pass
        else:
            updated_query = query_message.replace(" ", "+")
            try:
                await client.send_message(
                    chat_id=message.chat.id,
                    text=NO_MEDIA.format(query_message, updated_query),
                    reply_to_message_id=message.message_id,
                    parse_mode='html',
                    disable_web_page_preview=True
                )
            except Exception:
                pass
