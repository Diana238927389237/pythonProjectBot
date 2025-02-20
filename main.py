import telebot
from telebot import types
import random
TOKEN = '8010365849:AAEvQMxQ2MUGzeIPXhAQe2q9ZORrew4d3hY'



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Случайная книга')
    item2 = types.KeyboardButton('Хочу выбрать жанр')
    item3 = types.KeyboardButton('Личный кабинет')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Случайная книга':
            bot.send_message(message.chat.id, 'Ваша книга: ' + str(random.randint(0, 1000)))
        elif message.text == 'Хочу выбрать жанр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Книги российских авторов')
            item2 = types.KeyboardButton('Книги зарубежных авторов')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'Хочу выбрать жанр', reply_markup = markup)

        elif message.text == 'Книги на иностранных языках':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('English')
            item2 = types.KeyboardButton('Italiano')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'Хочу выбрать жанр', reply_markup = markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Случайная книга')
            item2 = types.KeyboardButton('Хочу выбрать жанр')
            item3 = types.KeyboardButton('Книги на иностранных языках')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id,'Назад', reply_markup=markup)


bot.polling(none_stop= True)