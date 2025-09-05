import time
import threading
import os
from flask import Flask
from telegram import Bot

# Load from environment variables, fallback to defaults if not set
BOT_TOKEN = os.getenv("BOT_TOKEN", "8467888370:AAEkb8Z0e8CX1dYj1rx2vV4_BlbM6KDwlUg")
MY_CHAT_ID = os.getenv("MY_CHAT_ID", "715202200")
FRIEND_CHAT_ID = os.getenv("FRIEND_CHAT_ID", "6193468045")

bot = Bot(token=BOT_TOKEN)

# Function to send messages every 15 minutes
def send_message():
    while True:
        text = "Hello Bangaram 💌"

        # Send to friend
        bot.send_message(chat_id=FRIEND_CHAT_ID, text=text)
        print("✅ Message sent to your friend!")

        # Send to you
        bot.send_message(chat_id=MY_CHAT_ID, text=text)
        print("✅ Message sent to you!")

        time.sleep(15 * 60)  # wait 15 minutes


# Flask server (keeps Render service alive)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running ✅"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    send_message()