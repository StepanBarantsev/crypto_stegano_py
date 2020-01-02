import telebot
from settings import config
import dbworker
import dbconfiguration
from Caesar import Caesar

bot = telebot.TeleBot(config["token"])


# This function handles the help command in the main menu
# STATE: MAIN
# COMMANDS: /help
# GOTO: MAIN
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == dbconfiguration.MAIN, commands=['help'])
def main_menu_helper(message):
    bot.send_message(message.chat.id, ''''List of available commands:
/help -- use this command to get a list of available commands
/caesar -- enter this command to go to Caesar mode''')


'''
@bot.message_handler(content_types=['document'])
def test_file_method(message):
    bot.send_message(message.chat.id, 'This is file to encrypt')
'''


# Function to go to the main menu from any state
# STATE: -
# COMMANDS: /start, /reset
# GOTO: MAIN
@bot.message_handler(commands=["start", "reset"])
def go_to_main(message):
    bot.send_message(message.chat.id, "You are in the Main Menu now")
    dbworker.set_state(message.chat.id, dbconfiguration.MAIN)
    # dbworker.clear_data(message.chat.id)


# Function to go to Caesar mode from any state
# STATE: -
# COMMANDS: /caesar
# GOTO: CAESAR
@bot.message_handler(commands=['caesar'])
def go_to_caesar_mode(message):
    bot.send_message(message.chat.id, "You are in the Caesar mode now")
    dbworker.set_state(message.chat.id, dbconfiguration.CAESAR)
    # dbworker.clear_data(message.chat.id)

###########################################################################
############################################################################
# CAESAR FUNCTIONS


def is_state_is_caesar(message):
    return dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR


# STATE: CAESAR
# COMMANDS: /help
# GOTO: CAESAR
@bot.message_handler(func=is_state_is_caesar, commands=['help'])
def caesar_helper(message):
    bot.send_message(message.chat.id, '''List of available commands:
/help -- use this command to get a list of available commands
/reset -- enter this command to go to main menu
encrypt or e -- enter this command to go to byte encryption mode
decrypt or d -- enter this command to go to byte decryption mode
encrypt_text or et -- enter this command to go to text encryption mode
decrypt_text or dt -- enter this command to go to text decryption mode''')


# STATE: CAESAR
# COMMANDS: encrypt, e
# GOTO: CAESAR_FILE_ENCRYPT

# STATE: CAESAR
# COMMANDS: decrypt, d
# GOTO: CAESAR_FILE_DECRYPT

# STATE: CAESAR
# COMMANDS: encrypt_text, et
# GOTO: CAESAR_FILE_ET

# STATE: CAESAR
# COMMANDS: decrypt_text, dt
# GOTO: CAESAR_FILE_DT

@bot.message_handler(func=is_state_is_caesar)
def caesar_go_to_any_mode(message):
    if message.text == 'e' or message.text == 'encrypt':
        bot.send_message(message.chat.id, '''You are in the CAESAR_FILE_ENCRYPT mode now''')
        bot.send_message(message.chat.id, '''Send me any file. If you want to send a photo, send it as a file!''')
        dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_FILE_ENCRYPT)

    elif message.text == 'd' or message.text == 'decrypt':
        bot.send_message(message.chat.id, '''You are in the CAESAR_FILE_DECRYPT mode now''')
        bot.send_message(message.chat.id, '''Send me any file. If you want to send a photo, send it as a file!''')
        dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_FILE_DECRYPT)

    elif message.text == 'et' or message.text == 'encrypt_text':
        bot.send_message(message.chat.id, '''You are in the CAESAR_FILE_ET mode now''')
        bot.send_message(message.chat.id, '''Send me txt file (ru or en lang).''')
        dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_FILE_ET)

    elif message.text == 'dt' or message.text == 'decrypt_text':
        bot.send_message(message.chat.id, '''You are in the CAESAR_FILE_DT mode now''')
        bot.send_message(message.chat.id, '''Send me txt file (ru or en lang).''')
        dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_FILE_DT)

    else:
        bot.send_message(message.chat.id, '''This is unknown command. 
Use the /help command to find out which commands are available.''')


# Get file method for byte algs
# STATE: CAESAR_FILE_ENCRYPT, CAESAR_FILE_DECRYPT
# COMMANDS: (No command, but input file)
# GOTO: CAESAR_SHIFT_ENCRYPT, CAESAR_SHIFT_DECRYPT
@bot.message_handler(func=lambda message:
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_ENCRYPT or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_DECRYPT,
                     content_types=['document', 'audio', 'video', 'photo', 'voice'])
def get_file(message):

    raw = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(raw.file_path)
    dbworker.set_data(message.chat.id, 'file', downloaded_file)
    bot.send_message(message.chat.id, '''Success (get file)!''')

    if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_ENCRYPT:
        bot.send_message(message.chat.id, '''You are in the CAESAR_SHIFT_ENCRYPT mode now''')
        dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_SHIFT_ENCRYPT)

    if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_DECRYPT:
        bot.send_message(message.chat.id, '''You are in the CAESAR_SHIFT_DECRYPT mode now''')
        dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_SHIFT_DECRYPT)

    bot.send_message(message.chat.id, '''Send me any natural number (this is your secret key).''')


# Get file method for text algs
# STATE: CAESAR_FILE_ET, CAESAR_FILE_DT
# COMMANDS: (No command, but input txt file)
# GOTO: CAESAR_SHIFT_ET, CAESAR_SHIFT_DT
@bot.message_handler(func=lambda message:
                     dbworker.get_current_state(message.chat.id) == dbconfiguration. CAESAR_FILE_ET or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_DT,
                     content_types=['document'])
def get_file_txt(message):
    if message.document.mime_type == 'text/plain':
        raw = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(raw.file_path)
        dbworker.set_data(message.chat.id, 'file', downloaded_file.decode('UTF-8'))
        bot.send_message(message.chat.id, '''Success (get txt file)!''')

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_ET:
            bot.send_message(message.chat.id, '''You are in the CAESAR_SHIFT_ET mode now''')
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_SHIFT_ET)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_DT:
            bot.send_message(message.chat.id, '''You are in the CAESAR_SHIFT_DT mode now''')
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_SHIFT_DT)

        bot.send_message(message.chat.id, '''Send me any natural number (this is your secret key).''')

    else:
        bot.send_message(message.chat.id, 'Document type must be txt!')


# If someone does not send a document
# STATE: CAESAR_FILE_ENCRYPT, CAESAR_FILE_DECRYPT, CAESAR_FILE_ET, CAESAR_FILE_DT
# COMMANDS: -
# GOTO: CAESAR_FILE_ENCRYPT, CAESAR_FILE_DECRYPT, CAESAR_FILE_ET, CAESAR_FILE_DT
@bot.message_handler(func=lambda message:
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_ENCRYPT or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_DECRYPT or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration. CAESAR_FILE_ET or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_FILE_DT,
                     content_types=['text', 'sticker', 'video_note', 'location', 'contact',
                                    'new_chat_members', 'left_chat_member', 'new_chat_title',
                                    'new_chat_photo', 'delete_chat_photo',
                                    'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                                    'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def error_file(message):
    bot.send_message(message.chat.id, '''So, you have to send only files!''')


# Get shift method
# STATE: CAESAR_SHIFT_ENCRYPT, CAESAR_SHIFT_DECRYPT, CAESAR_SHIFT_ET, CAESAR_SHIFT_DT
# COMMANDS: Any natural number
# GOTO: CAESAR, CAESAR, CAESAR_LANG_ET, CAESAR_LANG_DT
@bot.message_handler(func=lambda message:
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_ENCRYPT or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_DECRYPT or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_ET or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_DT)
def get_shift(message):
    try:
        shift = int(message.text)
        if shift <= 0:
            raise ValueError
    except ValueError:
        bot.send_message(message.chat.id, "Secret key must be natural number!")
    else:
        dbworker.set_data(message.chat.id, 'shift', shift)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_ENCRYPT:
            bot.send_message(message.chat.id, '''So, there is your output file!''')
            bot.send_document(message.chat.id, Caesar.encrypt(dbworker.get_data(message.chat.id, 'file'),
                                                              dbworker.get_data(message.chat.id, 'shift')))
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR)
            dbworker.clear_data(message.chat.id)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_DECRYPT:
            bot.send_message(message.chat.id, '''So, there is your output file!''')
            bot.send_document(message.chat.id, Caesar.decrypt(dbworker.get_data(message.chat.id, 'file'),
                                                              dbworker.get_data(message.chat.id, 'shift')))
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR)
            dbworker.clear_data(message.chat.id)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_ENCRYPT:
            bot.send_message(message.chat.id, '''You are in the CAESAR_LANG_ET mode now''')
            bot.send_message(message.chat.id, '''Input language (ru or en)!''')
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_LANG_ET)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_DECRYPT:
            bot.send_message(message.chat.id, '''You are in the CAESAR_LANG_DT mode now''')
            bot.send_message(message.chat.id, '''Input language (ru or en)!''')
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR_LANG_DT)


# Get lang method
# STATE: CAESAR_LANG_ET, CAESAR_LANG_DT
# COMMANDS: Any natural number
# GOTO: CAESAR, CAESAR
@bot.message_handler(func=lambda message:
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_ET or
                     dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_SHIFT_DT)
def get_lang(message):
    if message.text == 'ru' or message.text == 'en':
        bot.send_message(message.chat.id, "Language can be only en or ru!")
    else:
        dbworker.set_data(message.chat.id, 'lang', message.text)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_LANG_ET:
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR)
            bot.send_message(message.chat.id, '''So, there is your output file!''')
            bot.send_document(message.chat.id, Caesar.encrypt_text(dbworker.get_data(message.chat.id, 'file'),
                                                                   dbworker.get_data(message.chat.id, 'shift'),
                                                                   dbworker.get_data(message.chat.id, 'lang')))
            dbworker.clear_data(message.chat.id)

        if dbworker.get_current_state(message.chat.id) == dbconfiguration.CAESAR_LANG_DT:
            dbworker.set_state(message.chat.id, dbconfiguration.CAESAR)
            bot.send_message(message.chat.id, '''So, there is your output file!''')
            bot.send_document(message.chat.id, Caesar.encrypt_text(dbworker.get_data(message.chat.id, 'file'),
                                                                   dbworker.get_data(message.chat.id, 'shift'),
                                                                   dbworker.get_data(message.chat.id, 'lang')))
            dbworker.clear_data(message.chat.id)
    


############################################################################
# For any state it must be message about error!
@bot.message_handler(func=lambda message: True)
def any_error(message):
    bot.send_message(message.chat.id, 'Hello, this is unknown error. Read the instructions more carefully.')
    bot.send_message(message.chat.id, 'You are in %s mode now' % dbworker.get_current_state(message.chat.id))


############################################################################


if __name__ == '__main__':
    bot.polling(none_stop=True)
