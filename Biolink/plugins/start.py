from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def register(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(_, message: Message):
        await message.reply_text(
            f"👋 Hello {message.from_user.first_name}, welcome to Bio Mute Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("➕ Add me to your group", url="https://t.me/Aaradhyasongbot?startgroup=true")],
                    [InlineKeyboardButton("📢 Update Channel", url="https://t.me/shivang_xd")],
                    [InlineKeyboardButton("❓ Help", callback_data="help")]
                ]
            )
        )
