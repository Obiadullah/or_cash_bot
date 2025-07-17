import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Token নেয়া হচ্ছে environment variable থেকে
BOT_TOKEN = os.environ.get("7711618135:AAGb8F2a3bPCjIZp--eZ0Ym1cHpwVqtnkXI")

# ✅ /start কমান্ডের কাজ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 স্বাগতম! আমি O.R Cash Bot!")

# ✅ অ্যাপ তৈরি এবং হ্যান্ডলার অ্যাড
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# ✅ বট চালু করা
app.run_polling()
