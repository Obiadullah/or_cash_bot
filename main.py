from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "7711618135:AAGb8F2a3bPCjIZp--eZ0Ym1cHpwVqtnkXI"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 হ্যালো! আমি চালু আছি!")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
