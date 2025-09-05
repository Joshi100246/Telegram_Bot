from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Application, ContextTypes
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)

# Simple command handler
def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text('Hello! This bot is running with Flask and python-telegram-bot v20.3')

# Set up the telegram bot application
application = Application.builder().token(TELEGRAM_TOKEN).build()
application.add_handler(CommandHandler('start', start))

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        application.process_update(update)
        return 'ok'
    return 'invalid'

if __name__ == '__main__':
    # For local testing, run Flask app and polling
    import threading
    def run_flask():
        app.run(port=5000)
    t = threading.Thread(target=run_flask)
    t.start()
    application.run_polling()