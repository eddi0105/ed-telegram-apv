import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Команды бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 Привет! Я бот Эда - специалиста по работе с телом и психосоматикой.\n\n"
        "Я помогаю:\n"
        "• Убрать хронические боли через висцеральный массаж\n"
        "• Найти психологические причины физических симптомов\n"
        "• Разобрать натальную карту и понять свои циклы\n\n"
        "Выбери, что тебя интересует:\n"
        "/services - Мои услуги и цены\n"
        "/booking - Записаться на консультацию\n"
        "/contact - Связаться со мной\n"
        "/about - Обо мне"
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 МОИ УСЛУГИ:\n\n"
        "🔮 АСТРОЛОГИЯ - Натальная карта\n"
        "Разбор твоей карты, понимание циклов\n"
        "💰 3500₽ / 60 минут / онлайн\n\n"
        "🧠 ПСИХОСОМАТИКА\n"
        "Работа с психологическими причинами болей\n"
        "💰 3500₽ / 60 минут / онлайн или очно\n\n"
        "🤲 ВИСЦЕРАЛЬНЫЙ МАССАЖ\n"
        "Работа с внутренними органами через живот\n"
        "💰 3500₽ / 60 минут / только очно в Новосибирске\n"
        "💰 Курс 5 сеансов - 15000₽\n\n"
        "Для записи: /booking"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 КОНТАКТЫ:\n\n"
        "📱 Телефон: +7 913 919-01-05\n"
        "📧 Email: e2db@yandex.ru\n"
        "🌐 Сайт: edu-art.ru\n"
        "📍 Локация: Новосибирск (висцеральный массаж)\n"
        "💻 Онлайн: консультации по всему миру\n\n"
        "Отвечаю в течение 24 часов, обычно в течение 2-3 часов днём."
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 ОБО МНЕ:\n\n"
        "Меня зовут Эд. Я помогаю людям убрать хронические боли через работу с телом и психикой.\n\n"
        "Мой подход объединяет:\n"
        "• Астрологию (понимание жизненных циклов)\n"
        "• Психосоматику (связь тела и эмоций)\n"
        "• Висцеральную терапию (древняя техника массажа)\n\n"
        "Я сам прошёл через хроническую усталость и боли. Эти методы вернули мне энергию и желание жить. Теперь помогаю другим.\n\n"
        "Подробнее на сайте: edu-art.ru"
    )

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 ГДЕ Я ПРИНИМАЮ:\n\n"
        "🏢 Очно в Новосибирске:\n"
        "Висцеральный массаж - только очный формат\n\n"
        "💻 Онлайн из любой точки мира:\n"
        "• Разбор натальной карты\n"
        "• Психосоматические консультации\n\n"
        "Для записи: /booking"
    )

async def booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 ЗАПИСЬ НА КОНСУЛЬТАЦИЮ:\n\n"
        "Напиши мне в свободной форме:\n"
        "1. Что тебя беспокоит\n"
        "2. Какая услуга интересует\n"
        "3. Удобное время для связи\n\n"
        "Или позвони/напиши:\n"
        "📱 +7 913 919-01-05\n"
        "📧 e2db@yandex.ru\n\n"
        "Отвечу в течение 24 часов и предложу варианты времени."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if any(word in text for word in ['цена', 'стоимость', 'сколько', 'прайс']):
        await services(update, context)
    elif any(word in text for word in ['запись', 'записаться', 'консультация']):
        await booking(update, context)
    elif any(word in text for word in ['контакт', 'телефон', 'связь', 'позвонить']):
        await contact(update, context)
    else:
        await update.message.reply_text(
            "Я понял твой вопрос. Для быстрого ответа выбери команду из меню или напиши мне напрямую:\n"
            "📱 +7 913 919-01-05"
        )

def main():
    # Получаем токен из переменной окружения
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TOKEN:
        logger.error("Токен не найден!")
        return
    
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("services", services))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("location", location))
    application.add_handler(CommandHandler("booking", booking))
    
    # Обработчик обычных сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
