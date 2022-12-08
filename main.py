
from bot_command import *
from telegram.ext import Updater
from telegram.ext import CommandHandler
from configue import tg_token


updater = Updater(tg_token)
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('city', get_weather))


print('server start')
updater.start_polling()
updater.idle()

if __name__ == '__main__':
    updater.start_polling()