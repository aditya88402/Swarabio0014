from pyrogram import filters
from pyrogram.types import Message
from bot.config import OWNER_ID

def register(app):
    @app.on_message(filters.command("restart") & filters.user(OWNER_ID))
    async def restart_bot(_, message: Message):
        await message.reply("♻️ Restarting bot...")
        raise SystemExit
