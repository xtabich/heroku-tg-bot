import telebot
from telebot import types

bot = telebot.TeleBot('746437123:AAEdzEqrsFNuegQPrMFfwEEz23ZLTouGRLQ')

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Hello world')
	
if __name__ == '__main__':
    bot.polling()