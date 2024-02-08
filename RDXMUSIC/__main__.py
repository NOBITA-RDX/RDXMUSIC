import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RDXMUSIC import LOGGER, app, userbot
from RDXMUSIC.core.call import RDX
from RDXMUSIC.misc import sudo
from RDXMUSIC.plugins import ALL_MODULES
from RDXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("sᴛʀɪɴɢ sᴇssɪᴏɴ ɴᴏᴛ ғɪʟʟᴇᴅ, ᴘʟᴇᴀsᴇ ғɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RDXMUSIC.plugins" + all_module)
    LOGGER("RDXMUSIC.plugins").info("ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ʟᴏᴅᴇᴅ ʙᴀʙʏ.....")
    await userbot.start()
    await RDX.start()
    try:
        await RDX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("RDXMUSIC").error(
            "ᴘʟᴢᴢ sᴛᴀʀᴛ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ\ᴄʜᴀɴɴᴇʟ\n\ʀᴅx ʙᴏᴛ sᴛᴏᴘ........"
        )
        exit()
    except:
        pass
    await RDX.decorators()
    LOGGER("RDXMUSIC").info(
        "🥀 ᴍᴀᴅᴇ ʙʏ ʀᴅx ʀᴀᴊ🥀"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("RDXMUSIC").info("sᴛᴏᴘ ʀᴅx ᴍᴜsɪᴄ ♪ ʙᴏᴛ..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
