import os
from dotenv import load_dotenv
from telebot import TeleBot


load_dotenv()
bot = TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    text = 'Welcome to my bot from docker'
    bot.send_message(message.chat.id, text)

if __name__ == '__main__':
    bot.polling()