import telebot

bot = telebot.TeleBot("YOUR_TOKEN_HERE")

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