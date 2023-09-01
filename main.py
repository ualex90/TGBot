import copy

import telebot

from settings import TOKEN
from src.utils.utils import ChatLogger

logger = ChatLogger()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    logger.save_user(copy.deepcopy(message))
    mess = f'Хай <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    print(message.from_user.first_name, message.from_user.last_name)


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '<b><u>Ни че не знаю</u></b>', parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, f'{message.text}, долбаеб', parse_mode='html')
    print(message.from_user.first_name, message.from_user.last_name, message.chat.id)
    print(message.json['text'])


bot.polling(none_stop=True)
