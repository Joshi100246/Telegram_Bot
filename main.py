import asyncio
import threading
import os
from flask import Flask
from telegram import Bot

# Load from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "8467888370:AAHyaKjabwWY5zoHuojvMj_grUjo4WA_OAo")
MY_CHAT_ID = os.getenv("MY_CHAT_ID", "715202200")
FRIEND_CHAT_ID = os.getenv("FRIEND_CHAT_ID", "6193468045")

bot = Bot(token=BOT_TOKEN)

# Async message loop
async def send_message_async():
    while True:
        text = "Hello Bangaram 💌"
        try:
            # Send to friend
            await bot.send_message(chat_id=FRIEND_CHAT_ID, text=text)
            print("✅ Message sent to your friend!")

            # Send to you
            await bot.send_message(chat_id=MY_CHAT_ID, text=text)
            print("✅ Message sent to you!")

        except Exception as e:
            print(f"❌ Error sending message: {e}")

        await asyncio.sleep(15 * 60)  # wait 15 minutes


def start_message_loop():
    asyncio.run(send_message_async())


# Flask server (to keep Render alive)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running ✅"

def run_flask():
    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    # Run Flask server in background thread
    threading.Thread(target=run_flask).start()
    # Start async bot loop
    start_message_loop()
