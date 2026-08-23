import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Chào mừng! Bot đã hoạt động")

async def sanpham(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Danh sách sản phẩm")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sanpham", sanpham))
    print("Bot đang chạy...")
    app.run_polling()
