import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("Ошибка проверки токена бота")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привет! Я творение товарища @Letnyov. "
                                           "Мой творец является разработчиком на Python, "
                                           "разработчиком игр и видеомонтажером.")
    bot.send_message(message.chat.id, text="Доступные команды:\n /portfolio \n /skills")

@bot.message_handler(commands=['portfolio'])
def portfolio(message):
    bot.send_message(message.chat.id, text="Вот ссылки на ресурсы товарища @Letnyov: https://github.com/IGogga")

@bot.message_handler(commands=['skills'])
def skills(message):
    bot.send_message(message.chat.id, text="Список технологий - PyTelegramBotAPI, SQLite")


bot.infinity_polling()

