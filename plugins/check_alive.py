import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@Client.on_message(filters.command("credits", CMD))
async def credits(_, message):
    await message.reply_text("ᴛʜɪs ɪs ᴄᴏᴅᴇᴅ ʙʏ UNKNOWN")


@Client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("ғɪʀsᴛ ᴊᴏɪɴ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟ's, ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴀʙʟᴇ ᴛᴏ ᴜsᴇ ᴏᴜʀ ʙᴏᴛ ɪғ ʏᴏᴜ'ʀᴇ ᴍᴇᴍʙᴇʀ ᴏғ ᴛʜɪs ᴄʜᴀɴɴᴇʟ's. 👇 👇\n\n t.me/+u6G9wOGWt6Q4NTk1\n_______________________\n\nᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟ's, ᴛʏᴘᴇ ᴛʜᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ/sᴇʀɪᴇs ᴀɴᴅ ʏᴏᴜ'ʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴀᴅs. \n______________\n\n__________________\n\nɴᴏᴛᴇ:- ᴅᴏᴡɴʟᴏᴀᴅ ᴠʟᴄ ᴍᴇᴅɪᴀ ᴘʟᴀʏᴇʀ ꜰᴏʀ ʙᴇᴛᴛᴇʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
