import os
from dotenv import load_dotenv
import telebot

# Завантажуємо токен з .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Обробник: відповідає на будь-яке повідомлення тим самим текстом
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

# Запуск бота
bot.infinity_polling()
