from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RDXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

✦ ɪ ᴀᴍ ๛ʀ ᴅ x ༗

✦ ᴛʜɪs ɪs ʀᴅx ᴍᴜsɪᴄ ʙᴏᴛ ᴏғғɪᴄɪᴀʟ ʀᴇᴘᴏ.

✦ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ʀ ᴅ x ༗ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/+RObRa7kXPIJmMjU1"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/NOBITA-RDX/RDXMUSIC"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/33bc093c89898dcc318ae.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
