from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import MONGO_URI, MUTE_DURATION_HOURS
from datetime import datetime, timedelta
from pyrogram.enums import ChatPermissions

db = AsyncIOMotorClient(MONGO_URI).bio_mute
warns = db.warns

def is_link_or_username(text: str) -> bool:
    text = text.lower()
    return "http" in text or "t.me/" in text or "@" in text

async def add_warn(chat_id: int, user_id: int) -> int:
    user = await warns.find_one({"chat_id": chat_id, "user_id": user_id})
    if user:
        count = user["warns"] + 1
        await warns.update_one({"chat_id": chat_id, "user_id": user_id}, {"$set": {"warns": count}})
    else:
        count = 1
        await warns.insert_one({"chat_id": chat_id, "user_id": user_id, "warns": count})
    return count

async def get_warns(chat_id: int, user_id: int) -> int:
    user = await warns.find_one({"chat_id": chat_id, "user_id": user_id})
    return user["warns"] if user else 0

async def mute_user(client, chat_id, user_id, reason="", permanent=False, private_notify=False):
    until = None if permanent else datetime.utcnow() + timedelta(hours=MUTE_DURATION_HOURS)
    await client.restrict_chat_member(
        chat_id,
        user_id,
        ChatPermissions(),
        until_date=until
    )
    if not permanent:
        await client.send_message(chat_id, f"🔇 User muted for {MUTE_DURATION_HOURS} hours. Reason: {reason}")
    if private_notify:
        try:
            await client.send_message(user_id, f"You have been muted in {chat_id} due to: {reason}")
        except:
            pass
