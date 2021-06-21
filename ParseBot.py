import telebot
from telebot import types

#1722405488:AAE2d_kWr2ATBlC837NoVUsPXv3kq8ml4ok

#https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363

import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1722405488:AAE2d_kWr2ATBlC837NoVUsPXv3kq8ml4ok")

#mail
url = 'https://ru.investing.com/equities/mail.ru-grp-wi?cid=1163363'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='instrument-price_last__KQzyA')
for quote in quotes:
    mail = quote.text

#aeroflot
url = 'https://ru.investing.com/equities/aeroflot'
response1 = requests.get(url)
soup1 = BeautifulSoup(response1.text, 'lxml')
quotes1 = soup1.find_all('span', class_='instrument-price_last__KQzyA')
for quote1 in quotes1:
    aflt = quote1.text


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот \nЧтобы узнать о моих акциях вбей <b>/skills</b>".format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['skills'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("MAILDR")
    item2 = types.KeyboardButton("AFLT")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Что ты хочешь сделать?".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text =="MAILDR":
        bot.send_message(message.chat.id, "Стоимость акций Mail.ru Group Ltd (MAILDR) = "+mail)
    if message.text=="AFLT":
        bot.send_message(message.chat.id,"Стоимость акций ОАО Аэрофлот (AFLT) = "+aflt)


bot.polling()