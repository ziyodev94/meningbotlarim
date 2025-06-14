from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "7706373757:AAFaP4_GTS06Mmxe2bBDXk1hKNd1uH353hQ"
CHANNEL_URL = "https://t.me/sizning_kanalingiz"  # O'z kanalingiz URL manzili

# /start komandasi uchun
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Botga xush kelibsiz! Har qanday kontent yuboring. 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈")

# Barcha kontent turlari uchun handler
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    response_text = ""
    
    # Tugma yaratish
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Kanalga o'tish", url=CHANNEL_URL)]
    ])

    # Kontent turini aniqlash
    if message.document:
        response_text = f"📄 Fayl qabul qilindi!\nNomi: {message.document.file_name}"
    elif message.photo:
        response_text = f"🖼 Rasm qabul qilindi!\nHajmi: {message.photo[-1].file_size} bayt"
    elif message.video:
        response_text = f"🎥 Video qabul qilindi!\nDavomiylik: {message.video.duration} soniya"
    elif message.text and ("http://" in message.text or "https://" in message.text):
        response_text = f"🔗 Link qabul qilindi!\n{message.text}"
    elif message.text:
        response_text = f"✉️ Xabar qabul qilindi!\n{message.text}"
    else:
        response_text = "🔄 Kontent qabul qilindi!"

    # Javobni yuborish
    await message.reply_text(
        response_text + "\n\nQuyidagi tugma orqali kanalimizga qo'shiling:",
        reply_markup=keyboard
    )

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handlerlar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.PHOTO | filters.VIDEO | filters.Document.ALL | filters.TEXT,
        handle_messages
    ))
    
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
