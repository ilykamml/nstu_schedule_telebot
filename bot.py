import telebot

with open('token', 'r') as f:
    API = f.read()

bot = telebot.TeleBot(API)

