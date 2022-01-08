import os
import time

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Filters, MessageHandler, Updater

load_dotenv()

TOKEN_TELEGRAM = os.getenv('TELEGRAM_TOKEN')
updater = Updater(token=TOKEN_TELEGRAM)
bot = Bot(token=TOKEN_TELEGRAM)
chat_id_mar, chat_id_my = 1064278386, 1803284378
RETRY_TIME = 10


def say_hi(update, context):
    text_message = update.message.text
    context.bot.send_message(chat_id=chat_id_my, text=text_message)


while True:
    try:
        text = 'Съешь курагу и изюм!'
        bot.send_message(chat_id_my, text)
        updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
        updater.start_polling()
    except Exception:
        print('Ошибка отправки')
        time.sleep(5)
    else:
        time.sleep(RETRY_TIME)
