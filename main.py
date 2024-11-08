from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, Application, ApplicationBuilder

# создаем экземпляр Bot
bot = Bot(token="6994142818:AAFnemVStle9xIqnHFTz-SpIQGh63huIRGQ")

# создаем приложение
app = ApplicationBuilder().token("6994142818:AAFnemVStle9xIqnHFTz-SpIQGh63huIRGQ").build()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я ваш бот.")

start_handler = CommandHandler('start', start)
app.add_handler(start_handler)

# запускаем бота
app.run_polling()
