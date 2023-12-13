# -*- coding: cp1251 -*-
import telebot
chat_id = '665515513'
bot = telebot.TeleBot('5885707851:AAEiOBjsY_y0K4RDX4aQUaqKkyZakFmbJWw')
from telebot import types

@bot.message_handler(content_types=['str'])
def get_text_messages(message, id):
    text = message
    chat_id = id
    if text == "Работать":
        bot.send_message(chat_id, "Вошёл в цикл работы и начал Заклить")
    else:
        bot.send_message(chat_id, "Работать не с чем !!!! Нечего заклинать")

def get_text_while(message, id):
    text = message
    chat_id = id
    bot.send_message(chat_id, text)



