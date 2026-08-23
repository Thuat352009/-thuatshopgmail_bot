from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8895421064:AAFC8CzFgXHwNjaz96d5cMKAWgBIv1tWhfU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Chào mừng đến Thuật Shop! \nGõ /sanpham để xem sản phẩm")

async def sanpham(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Danh sách sản phẩm:\n1. Sản phẩm A - 100k\n2. Sản phẩm B - 200k\n\nLiên hệ đặt hàng nhé!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sanpham", sanpham))
print("Bot đang chạy...")
app.run_polling()
