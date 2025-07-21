from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN
from bot.handlers import start_handler
from bot.plugins import welcome, moderation, broadcast, owner
from bot.plugins import callback

app = Client(
    "bio_mute_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
start_handler.register(app)
welcome.register(app)
moderation.register(app)
broadcast.register(app)
owner.register(app)
callback.register(app)

print("🤖 Bio Mute Bot is running...")
app.run()
