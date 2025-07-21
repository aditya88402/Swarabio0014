from pyrogram import filters
from pyrogram.types import Message
from bot.config import OWNER_ID

def register(app):
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast(_, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a message to broadcast.")
        # Broadcast logic here
        await message.reply("✅ Broadcast started (placeholder).")
