# -*- coding: cp1251 -*-
import telebot
chat_id = '665515513'
bot = telebot.TeleBot('5885707851:AAEiOBjsY_y0K4RDX4aQUaqKkyZakFmbJWw')
from telebot import types

@bot.message_handler(content_types=['str'])
def get_text_messages(message, id):
    text = message
    chat_id = id
    if text == "��������":
        bot.send_message(chat_id, "����� � ���� ������ � ����� �������")
    else:
        bot.send_message(chat_id, "�������� �� � ��� !!!! ������ ���������")

def get_text_while(message, id):
    text = message
    chat_id = id
    bot.send_message(chat_id, text)



