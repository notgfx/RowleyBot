import telebot
import sqlite3
import random

from telebot import types
bot = telebot.TeleBot('597467998:AAHdrNb5iz_ZT0C5EJAvuVR1Mq0omNvL0no')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, False)
keyboard1.row('/start','Привет', 'Пока', 'Я тебя люблю')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else:
        bot.send_message(message.chat.id, 'Rainhard behind!')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()