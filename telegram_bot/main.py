import telebot
from settings import config
from Caesar import Caesar

bot = telebot.TeleBot(config["token"])


@bot.message_handler(commands=['help'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, '''Hello, this is help article''')


@bot.message_handler(content_types=['document'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, 'This is file to encrypt')


if __name__ == '__main__':
    bot.polling(none_stop=True)
