import re
import os
import time

from base64 import b64decode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from utils.file_size import get_size

CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
ASK_PM_TEXT = "<b>Click the below button</b>"

CHANNELS = -1002145296820

@Client.on_message(filters.private & filters.text)
async def snd_pm(client, message):
      if secret_query:
          for channel in CHANNELS:
              # Looking for Document type in messages
              async for messages in client.USER.search_messages(channel, secret_query, filter="document", limit=50):
                  doc_file_names = messages.document.file_name
                  file_size = get_size(messages.document.file_size)
                  if re.compile(rf'{doc_file_names}', re.IGNORECASE):
                      media_name = messages.document.file_name.rsplit('.', 1)[0]
                      media_format = messages.document.file_name.split('.')[-1]
                      await client.send_chat_action(
                          chat_id=message.from_user.id,
                          action="upload_document"
                      )
                      try:
                          await client.copy_message(
                              chat_id=message.chat.id,
                              from_chat_id=messages.chat.id,
                              message_id=messages.message_id,
                              caption=GROUP_U_NAME+CAPTION_TEXT_DOC.format(media_name,
                                                                                            media_format, file_size)
                          )
                      except FloodWait as e:
                          time.sleep(e.x)
              # Looking for video type in messages
              async for messages in client.USER.search_messages(channel, secret_query, filter="video", limit=50):
                  vid_file_names = messages.caption
                  file_size = get_size(messages.video.file_size)
                  if re.compile(rf'{vid_file_names}', re.IGNORECASE):
                      media_name = secret_query.upper()
                      await client.send_chat_action(
                          chat_id=message.from_user.id,
                          action="upload_video"
                      )
                      try:
                          await client.copy_message(
                              chat_id=message.chat.id,
                              from_chat_id=messages.chat.id,
                              message_id=messages.message_id,
                              caption=GROUP_U_NAME+CAPTION_TEXT_VID.format(media_name, file_size)
                          )
                      except FloodWait as e:
                          time.sleep(e.x)
