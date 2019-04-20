import telebot

bot = telebot.TeleBot('860528282:AAGR6kaJ_K4RYlzJo8fXgZsDdrcFAW9N-lw')

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message, message.text)

bot.polling()
