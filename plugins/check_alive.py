import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@Client.on_message(filters.command("credits", CMD))
async def credits(_, message):
    await message.reply_text("ᴛʜɪs ɪs ᴄᴏᴅᴇᴅ ʙʏ @Waldy_Writings")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n𝗠𝗼𝘃𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ғʀᴏᴍ ɢᴏᴏɢʟᴇ ➠ ᴘᴀsᴛᴇ ᴄᴏᴘɪᴇᴅ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : sᴀᴍᴀᴊᴀᴠᴀʀᴀɢᴀᴍᴀɴᴀ 2023 ᴇʟᴀ ɴᴀᴍᴇ ᴀɴᴅ ʏᴇᴀʀ ᴘᴇᴛᴀɴᴅɪ\n\n🚯 ᴅᴏɴᴛ ᴛʏᴘᴇ ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛ 🤧 ➠ :(ʟᴀɴɢᴜᴀɢᴇ ᴍᴇɴᴛɪᴏɴ ᴄʜᴇʏᴀᴋᴀɴᴅɪɪ,ᴀɴᴅ ᴍᴀɪɴ ᴛʜɪɴɢ ᴛʜᴇᴀᴛʀᴇ ᴘʀɪɴᴛs ᴀʀᴇ ɴᴏᴛ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴏᴜʀ ʙᴏᴛ⚠️⚠️))\n\nᴄᴏᴅᴇᴅ ʙʏ @Waldy_Writings")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n𝗦𝗲𝗿𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ sᴇʀɪᴇs ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ sᴇʀɪᴇs ɴᴀᴍᴇ ᴀᴅᴅ sᴇᴀsᴏɴ ɴᴜᴍʙᴇʀ ʟɪᴋᴇ s01 ʙᴇsɪᴅᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴘᴀsᴛᴇ ᴄᴏᴘɪᴇᴅ sᴇʀɪᴇs ɴᴀᴍᴇ ᴡɪᴛʜ sᴇᴀsᴏɴ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴍᴏɴᴇʏ ʜᴇɪsᴛ s01ᴇ01\n\n🙅‍♂️🙅‍♂️ᴅᴏɴᴛ ᴛʏᴘᴇ ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛ ➠ ':(ᴍᴏɴᴇʏ ʜᴇɪsᴛ sᴇᴀsᴏɴ 1,ᴇʟᴀ ᴛʏᴘᴇ ᴄʜᴇsᴛʜᴇ ʀᴀᴠᴜ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ғᴏʀᴍᴀᴛ ʟᴏ ᴘᴀᴍᴘᴀʟɪ ᴘᴀɪɴᴀ ғᴏʀᴍᴀᴛ ᴄʜᴜᴅᴀɴᴅɪ ) )\n\nᴄᴏᴅᴇᴅ ʙʏ @Waldy_Writings")

@Client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("ғɪʀsᴛ ᴊᴏɪɴ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴀʙʟᴇ ᴛᴏ ᴜsᴇ ᴏᴜʀ ʙᴏᴛ ɪғ ʏᴏᴜʀᴇ ᴍᴇᴍʙᴇʀ ᴏғ ᴛʜɪs ᴄʜᴀɴɴᴇʟs. 👇\n\n  http://t.me/Waldy_Writings\nhttp://t.me/waldy_writings2\n_______________________\n\nᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs ᴛʏᴘᴇ ᴛʜᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ/sᴇʀɪᴇs ᴀɴᴅ ʏᴏᴜʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴀᴅs\n______________\n\nCᴏʀʀᴇᴄᴛ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /movies\n__________________\n\nCᴏʀʀᴇᴄᴛ Sᴇʀɪᴇs Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /series\n__________________\n\nɴᴏᴛᴇ:- ᴅᴏᴡɴʟᴏᴀᴅ ᴠʟᴄ ᴍᴇᴅɪᴀ ᴘʟᴀʏᴇʀ ꜰᴏʀ ʙᴇᴛᴛᴇʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
