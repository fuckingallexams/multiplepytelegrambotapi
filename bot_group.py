# coding=utf-8
import sys,time,os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#groupmode
bot = telebot.TeleBot(sys.argv[1])
me = bot.get_me()
     
@bot.message_handler(func=lambda message : message.chat.type == "private")
def private_message_handler(message):
    bot.send_message(message.chat.id,"fucking all exams",parse_mode = "HTML",disable_web_page_preview=True)
   
print("fucking all exams")
bot.polling(True)
