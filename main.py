import os
from dotenv import load_dotenv
from telebot import TeleBot


load_dotenv()

bot = TeleBot(os.getenv('BOT_TOKEN'))
tasks = list()

@bot.message_handler(commands=['start'])
def start(message):
    text = 'Welcome to my bot from docker'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['get_tasks'])
def get_tasks(message):
    text = ''
    for task in tasks:
        text += (f"User: {task['chat_id']}\n\n"
                f"Title: {task['title']}\n\n"
                f"Task: {task['text']}\n\n")

    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: True)
def add_task(message: dict):
    command, title, task = message.text.split('\n\n')

    if command == 'add':
        tasks.append({
            'chat_id': message.chat.id,
            'title': title,
            'text': task
        })

if __name__ == '__main__':
    bot.polling()