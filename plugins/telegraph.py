import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from YukkiMusic import app

@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ"
        )
    if message.reply_to_message.sticker:
        sticker = message.reply_to_message.sticker
        if sticker.is_video or not sticker.is_animated:
            try:
                text = await message.reply("downloading sticker.")
                file_path = await app.download_media(sticker.file_id, file_name=f"{sticker.file_id}_sticker.png")
                upload_path = upload_file(file_path)
                await text.edit_text(f"🌐 | [ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ](https://telegra.ph{upload_path[0]})",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ",url=f"https://telegra.ph{upload_path[0]}")]]))
                try:
                    os.remove(local_path)
                    os.remove(file_path)
                except Exception:
                   pass
            except Exception as e:
                await text.edit_text(f"❌ |ғɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ \n\n<i>ʀᴇᴀsᴏɴ: {e}</i>")
                try:
                    os.remove(local_path)
                    os.remove(file_path)
                except Exception:
                   pass
    else:
        try:
            text = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
            async def progress(current, total):
                await text.edit_text(f"📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ... {current * 100 / total:.1f}%")
            try:
                local_path = await message.reply_to_message.download( progress=progress
                )
                await text.edit_text("📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
                upload_path = upload_file(local_path)
                await text.edit_text(
                f"🌐 | [ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                            [
                                InlineKeyboardButton(
                                    "ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ",
                                    url=f"https://telegra.ph{upload_path[0]}",
                                )
                            ]
                        ]
                    ),
                )
                try:
                    os.remove(local_path)
                except Exception:
                   pass
            except Exception as e:
                await text.edit_text(f"❌ |ғɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ \n\n<i>ʀᴇᴀsᴏɴ: {e}</i>")
                try:
                    os.remove(local_path)
                except Exception:
                   pass
        except Exception:
            pass

__HELP__ = """
**ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ:

- `/tgm`: ᴜᴘʟᴏᴀᴅ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.
- `/tgt`: sᴀᴍᴇ ᴀs `/tgm`.
- `/telegraph`: sᴀᴍᴇ ᴀs `/tgm`.
- `/tl`: sᴀᴍᴇ ᴀs `/tgm`.

**ᴇxᴀᴍᴘʟᴇ:**
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ `/tgm` ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ.

**ɴᴏᴛᴇ:**
ʏᴏᴜ ᴍᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴡᴏʀᴋ.
"""

__MODULE__ = "Tᴇʟᴇɢʀᴀᴘʜ"