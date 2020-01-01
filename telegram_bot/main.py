import telebot
from settings import config
import dbworker
import dbconfiguration
from Caesar import Caesar

bot = telebot.TeleBot(config["token"])


# This function handles the help command in the main menu
# STATE: MAIN
# COMMANDS: HELP
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == dbconfiguration.MAIN, commands=['help'])
def main_menu_helper(message):
    bot.send_message(message.chat.id, '''Hello, this is main menuvhelp article''')


'''
@bot.message_handler(content_types=['document'])
def test_file_method(message):
    bot.send_message(message.chat.id, 'This is file to encrypt')
'''


# Function to go to the main menu from any state
# STATE: -
# COMMANDS: /start, /reset
@bot.message_handler(commands=["start", "reset"])
def go_to_main(message):
    bot.send_message(message.chat.id, "You are in the Main Menu now")
    dbworker.set_state(message.chat.id, dbconfiguration.MAIN)


# Function to go to Caesar mode from any state
# STATE: -
# COMMANDS: /caesar
@bot.message_handler(commands=['caesar'])
def go_to_caesar_mode(message):
    bot.send_message(message.chat.id, "You are in the Caesar mode now")
    dbworker.set_state(message.chat.id, dbconfiguration.CAESAR)


if __name__ == '__main__':
    bot.polling(none_stop=True)
