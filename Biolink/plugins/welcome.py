from pyrogram import filters
from pyrogram.types import Message
from bot.utils.database import mute_user, is_link_or_username
from bot.config import OWNER_ID

def register(app):
    @app.on_message(filters.new_chat_members)
    async def handle_new_member(client, message: Message):
        for user in message.new_chat_members:
            if is_link_or_username(user.first_name):
                await mute_user(client, message.chat.id, user.id, reason="Bio contains link/username", permanent=True, private_notify=True)
