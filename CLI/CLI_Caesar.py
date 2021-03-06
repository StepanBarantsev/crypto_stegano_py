import sys
import os
from CLI_Helper import CLI_Helper

# We can't import class from another folder without this line
sys.path.append('../')

from crypto_algs.Caesar import Caesar


class CLI_Caesar:

    def __init__(self):
        pass

    @staticmethod
    def start():
        os.system('cls' if os.name == 'nt' else 'clear')
        command = None
        while command != 'return':
            print('Hello, you are is Caesar mode')
            print('You can get help with the command: Help')
            print('You can return to main menu with the command: Return')
            print()
            command = input('[Caesar] Enter command: ').lower()
            print()
            if command == 'help':
                CLI_Caesar.print_available_commands()
            elif command == 'return':
                os.system('cls' if os.name == 'nt' else 'clear')
                return
            elif command == 'encrypt' or command == 'e':
                CLI_Caesar.encrypt()
            elif command == 'decrypt' or command == 'd':
                CLI_Caesar.decrypt()
            elif command == 'decrypt_without_shift' or command == 'dws':
                CLI_Caesar.decrypt_without_shift()
            elif command == 'encrypt_text' or command == 'et':
                CLI_Caesar.encrypt_text()
            elif command == 'decrypt_text' or command == 'dt':
                CLI_Caesar.decrypt_text()
            elif command == 'decrypt_text_without_shift' or command == 'dtws':
                CLI_Caesar.decrypt_text_without_shift()
            else:
                print('Unknown command')
            CLI_Caesar.print_press_enter_and_clear_screen()

    @staticmethod
    def print_available_commands():
        print('List of available commands:')
        print('Help -- use this command to get a list of available commands')
        print('Return -- enter this command to go to main menu')
        print('Encrypt or e -- enter this command to go to byte encryption mode')
        print('Decrypt or d -- enter this command to go to byte decryption mode')
        print("Decrypt_without_shift or dws -- enter this command to go to byte decryption mode if you don't know key")
        print('Encrypt_text or et -- enter this command to go to text encryption mode')
        print('Decrypt_text or dt -- enter this command to go to text decryption mode')
        print("Decrypt_text_without_shift or dtws -- enter this command to go to text decryption mode if you don't know key")

    @staticmethod
    def encrypt():
        os.system('cls' if os.name == 'nt' else 'clear')
        CLI_Caesar.print_info_about_encryption_mode()
        # If user wan't to stop this func we use this variable
        ret_flag = [False]
        filename = CLI_Helper.read_correct_filename(ret_flag,
                                                    '[Caesar][Encrypt] Enter the full path to the file you want to encrypt (with extension): ',
                                                    'e', CLI_Caesar)
        if ret_flag[0]:
            return
        shift = CLI_Helper.read_correct_shift(ret_flag,
                                              '[Caesar][Encrypt] Enter any natural number (this is secret key): ',
                                              'e', CLI_Caesar)
        if ret_flag[0]:
            return
        # At this step, we believe that we have the correct file name and shift
        with open(filename, 'rb') as f:
            seq = f.read()
            # There is directory for saving encrypted file
            extension, path_to_file = CLI_Helper.get_file_extension_and_file_path(filename)
            with open(path_to_file + 'output.' + extension, 'wb') as g:
                g.write(Caesar.encrypt(seq, shift))

        print()
        print('Encryption was successful. You can see result in the file named output.' + extension)

    @staticmethod
    def print_info_about_encryption_mode():
        print('Hello -- You are in the Caesar Encryption mode now. Enter Return to go to Caesar mode.')
        print('If you want to encrypt data, follow the instructions in the program.')
        print()

    @staticmethod
    def clear_screen_and_print_info_about_mode(mode):
        CLI_Caesar.print_press_enter_and_clear_screen()
        if mode == 'e':
            CLI_Caesar.print_info_about_encryption_mode()
        elif mode == 'd':
            CLI_Caesar.print_info_about_decryption_mode()
        elif mode == 'dws':
            CLI_Caesar.print_info_about_dws_mode()
        elif mode == 'et':
            CLI_Caesar.print_info_about_et_mode()
        elif mode == 'dt':
            CLI_Caesar.print_info_about_dt_mode()
        elif mode == 'dtws':
            CLI_Caesar.print_info_about_dtws_mode()

    @staticmethod
    def print_press_enter_and_clear_screen():
        print()
        input('Press Enter')
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def decrypt():
        os.system('cls' if os.name == 'nt' else 'clear')
        CLI_Caesar.print_info_about_decryption_mode()
        # If user wan't to stop this func we use this variable
        ret_flag = [False]
        filename = CLI_Helper.read_correct_filename(ret_flag,
                                                    '[Caesar][Decrypt] Enter the full path to the file you want to decrypt (with extension): ',
                                                    'd', CLI_Caesar)
        if ret_flag[0]:
            return
        shift = CLI_Helper.read_correct_shift(ret_flag,
                                              '[Caesar][Decrypt] Enter any natural number (this is secret key): ',
                                              'd', CLI_Caesar)
        if ret_flag[0]:
            return
        # At this step, we believe that we have the correct file name and shift
        with open(filename, 'rb') as f:
            seq = f.read()
            # There is directory for saving encrypted file
            extension, path_to_file = CLI_Helper.get_file_extension_and_file_path(filename)
            with open(path_to_file + 'output.' + extension, 'wb') as g:
                g.write(Caesar.decrypt(seq, shift))
        print()
        print('Decryption was successful. You can see result in the file named output.' + extension)

    @staticmethod
    def print_info_about_decryption_mode():
        print('Hello -- You are in the Caesar Decryption mode now. Enter Return to go to Caesar mode.')
        print('If you want to decrypt data, follow the instructions in the program.')
        print()

    @staticmethod
    def decrypt_without_shift():
        os.system('cls' if os.name == 'nt' else 'clear')
        CLI_Caesar.print_info_about_dws_mode()
        # If user wan't to stop this func we use this variable
        ret_flag = [False]
        filename = CLI_Helper.read_correct_filename(ret_flag,
                                                    '[Caesar][Dws] Enter the full path to the file you want to decrypt (with extension): ',
                                                    'dws', CLI_Caesar)
        if ret_flag[0]:
            return

        # At this step, we believe that we have the correct file name
        with open(filename, 'rb') as f:
            seq = f.read()
            # There is directory for saving encrypted file
            extension, path_to_file = CLI_Helper.get_file_extension_and_file_path(filename)
            lst = Caesar.decrypt_without_shift(seq)
            for i, element in enumerate(lst):
                with open(path_to_file + 'output%s.' % i + extension, 'wb') as g:
                    g.write(element)

        print()
        print('Decryption was successful. You can see result in the file named output.' + extension)

    @staticmethod
    def print_info_about_dws_mode():
        print('Hello -- You are in the Caesar Decryption without shift mode now. Enter Return to go to Caesar mode.')
        print('If you want to decrypt data, follow the instructions in the program.')
        print()

    @staticmethod
    def encrypt_text():
        os.system('cls' if os.name == 'nt' else 'clear')
        CLI_Caesar.print_info_about_et_mode()
        # If user wan't to stop this func we use this variable
        ret_flag = [False]

        filename = CLI_Helper.read_correct_filename_with_extension_check(ret_flag,
                                                    '[Caesar][Encrypt txt] Enter the full path to the file you want to encrypt (with extension): ',
                                                    'e', 'txt', CLI_Caesar)
        if ret_flag[0]:
            return

        shift = CLI_Helper.read_correct_shift(ret_flag,
                                              '[Caesar][Encrypt txt] Enter any natural number (this is secret key): ',
                                              'e', CLI_Caesar)
        if ret_flag[0]:
            return
        lang = CLI_Helper.read_correct_lang(ret_flag,
                                            '[Caesar][Encrypt txt] Enter language (ru or en): ', 'et', CLI_Caesar)
        if ret_flag[0]:
            return
        # At this step, we believe that we have the correct file name, shift and lang
        with open(filename, 'r', encoding='UTF-8') as f:
            txt = f.read()
            # There is directory for saving encrypted file
            extension, path_to_file = CLI_Helper.get_file_extension_and_file_path(filename)
            with open(path_to_file + 'output.' + extension, 'w', encoding='UTF-8') as g:
                g.write(Caesar.encrypt_text(txt, shift, lang))

        print()
        print('Encryption was successful. You can see result in the file named output.' + extension)

    @staticmethod
    def print_info_about_et_mode():
        print('Hello -- You are in the Caesar Encryption text mode now. Enter Return to go to Caesar mode.')
        print('If you want to encrypt text, follow the instructions in the program.')
        print()

    @staticmethod
    def decrypt_text():
        os.system('cls' if os.name == 'nt' else 'clear')
        CLI_Caesar.print_info_about_dt_mode()
        # If user wan't to stop this func we use this variable
        ret_flag = [False]

        filename = CLI_Helper.read_correct_filename_with_extension_check(ret_flag,
                                                         '[Caesar][Decrypt txt] Enter the full path to the file you want to encrypt (with extension): ',
                                                         'dt', 'txt', CLI_Caesar)
        if ret_flag[0]:
            return

        shift = CLI_Helper.read_correct_shift(ret_flag,
                                              '[Caesar][Decrypt txt] Enter any natural number (this is secret key): ',
                                              'dt', CLI_Caesar)
        if ret_flag[0]:
            return
        lang = CLI_Helper.read_correct_lang(ret_flag,
                                            '[Caesar][Decrypt txt] Enter language (ru or en): ', 'dt', CLI_Caesar)
        if ret_flag[0]:
            return
        # At this step, we believe that we have the correct file name, shift and lang
        with open(filename, 'r', encoding='UTF-8') as f:
            txt = f.read()
            # There is directory for saving encrypted file
            extension, path_to_file = CLI_Helper.get_file_extension_and_file_path(filename)
            with open(path_to_file + 'output.' + extension, 'w', encoding='UTF-8') as g:
                g.write(Caesar.decrypt_text(txt, shift, lang))

        print()
        print('Decryption was successful. You can see result in the file named output.' + extension)

    @staticmethod
    def print_info_about_dt_mode():
        print('Hello -- You are in the Caesar Decryption text mode now. Enter Return to go to Caesar mode.')
        print('If you want to decrypt text, follow the instructions in the program.')
        print()

    @staticmethod
    def decrypt_text_without_shift():
        os.system('cls' if os.name == 'nt' else 'clear')
        CLI_Caesar.print_info_about_dtws_mode()
        # If user wan't to stop this func we use this variable
        ret_flag = [False]
        filename = CLI_Helper.read_correct_filename_with_extension_check(ret_flag,
                                                    '[Caesar][Dtws] Enter the full path to the file you want to decrypt (with extension): ',
                                                    'dtws', 'txt', CLI_Caesar)
        if ret_flag[0]:
            return

        lang = CLI_Helper.read_correct_lang(ret_flag,
                                            '[Caesar][Dtws] Enter language (ru or en): ', 'dtws', CLI_Caesar)
        if ret_flag[0]:
            return

        # At this step, we believe that we have the correct file name
        with open(filename, 'r', encoding='UTF-8') as f:
            txt = f.read()
            # There is directory for saving encrypted file
            extension, path_to_file = CLI_Helper.get_file_extension_and_file_path(filename)
            lst = Caesar.decrypt_text_without_shift(txt, lang)
            for i, element in enumerate(lst):
                with open(path_to_file + 'output%s.' % i + extension, 'w', encoding='UTF-8') as g:
                    g.write(element)

        print()
        print('Decryption was successful. You can see result in the file named output.' + extension)

    @staticmethod
    def print_info_about_dtws_mode():
        print('Hello -- You are in the Caesar Decryption text without shift mode now. Enter Return to go to Caesar mode.')
        print('If you want to decrypt text, follow the instructions in the program.')
        print()
