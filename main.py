import os 
import telebot

bot = telebot.TeleBot("API key here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"hello!i'am yk creation bot")

    @bot.message_handler(commands=["how"])
    def send_message(message):
        bot.send_message(message,"htps//youtube.com/ch/ykcreation")

bot.polling()