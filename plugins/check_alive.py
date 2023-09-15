import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

app = Client(
    "your_session_name",
    bot_token="your_bot_token",
    api_id=your_api_id,
    api_hash="your_api_hash"
)

# Define your API ID and API Hash here

@app.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@app.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@app.on_message(filters.command("credits", CMD))
async def credits(_, message):
    await message.reply_text("ᴛʜɪs ɪs ᴄᴏᴅᴇᴅ ʙʏ KKMOVIES")

@app.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("ғɪʀsᴛ ᴊᴏɪɴ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs, ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴀʙʟᴇ ᴛᴏ ᴜsᴇ ᴏᴜʀ ʙᴏᴛ ɪғ ʏᴏᴜʀᴇ ᴍᴇᴍʙᴇʀ ᴏғ ᴛʜɪs ᴄʜᴀɴɴᴇʟs. 👇👇 \n\n http://t.me/+u6G9wOGWt6Q4NTk1\n_______________________\n\nᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs ᴛʏᴘᴇ ᴛʜᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ/sᴇʀɪᴇs ᴀɴᴅ ʏᴏᴜʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴀᴅs\n______________\n\nɴᴏᴛᴇ:- ᴅᴏᴡɴʟᴏᴀᴅ ᴠʟᴄ ᴍᴇᴅɪᴀ ᴘʟᴀʏᴇʀ ꜰᴏʀ ʙᴇᴛᴛᴇʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ")

@app.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")

if __name__ == "__main__":
    app.run()
