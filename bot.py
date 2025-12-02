import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 Привет! Я бот Эда - специалиста по APV методу.\n\n"
        "/services - Мои услуги и цены\n"
        "/booking - Записаться на консультацию\n"
        "/contact - Связаться со мной"
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 МОИ УСЛУГИ:\n\n"
        "🔮 АСТРОЛОГИЯ - 3500₽\n"
        "🧠 ПСИХОСОМАТИКА - 3500₽\n"
        "🤲 ВИСЦЕРАЛЬНЫЙ МАССАЖ - 3500₽\n\n"
        "📱 +7 913 919-01-05"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 КОНТАКТЫ:\n"
        "📱 +7 913 919-01-05\n"
        "📧 e2db@yandex.ru\n"
        "🌐 edu-art.ru"
    )

async def booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Для записи позвоните:\n"
        "📱 +7 913 919-01-05"
    )

def main():
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    PORT = int(os.environ.get('PORT', 10000))
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("booking", booking))
    
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="",
        webhook_url=f"{os.environ.get('RENDER_EXTERNAL_URL')}"
    )

if __name__ == '__main__':
    main()
