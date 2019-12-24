# This is command line interface
import sys
import os

# We can't import class from another folder without this line
sys.path.append('../')

from crypto_algs.Caesar import Caesar


class CLI:

    def __init__(self):
        pass

    @staticmethod
    def start():
        command = None
        while command != 'stop':
            print('Hello, You are now in the main menu')
            print('You can get help with the command: Help')
            print()
            command = input('Enter command: ').lower()
            print()
            if command == 'help':
                CLI.print_available_commands()
            elif command == 'caesar':
                CLI.start_caesar_mode()
                continue
            else:
                print('Unknown command')
            print()
            # Empty input so that the text is not overwritten immediately
            input('Press Enter')
            os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_available_commands():
        print('List of available commands:')
        print('Help -- use this command to get a list of available commands')
        print('Caesar -- enter this command to go to Caesar mode')

    @staticmethod
    def start_caesar_mode():
        CLI_Caesar.start()


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
            print()
            # Empty input so that the text is not overwritten immediately
            input('Press Enter')
            os.system('cls' if os.name == 'nt' else 'clear')

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
        filename = CLI_Caesar.read_correct_filename(ret_flag)
        if ret_flag[0]:
            return
        shift = CLI_Caesar.read_correct_shift(ret_flag)
        if ret_flag[0]:
            return
        # At this step, we believe that we have the correct file name and shift
        with open(filename, 'rb') as f:
            seq = f.read()
            # There is directory for saving encrypted file
            path_to_file = filename.replace(os.path.basename(filename), '')
            extension = os.path.basename(filename).split('.')[1]
            with open(path_to_file + 'output.' + extension, 'wb') as g:
                g.write(Caesar.encrypt(seq, shift))

        print()
        print('Encryption was successful. You can see result in the file named output' + extension)

    @staticmethod
    def print_info_about_encryption_mode():
        print('Hello -- You are in the Caesar Encryption mode now. Enter Return to go to Caesar mode.')
        print('If you want to encrypt data, follow the instructions in the program.')
        print()

    @staticmethod
    def read_correct_shift(ret_flag):
        shift = None
        while shift is None:
            shift = input('[Caesar][Encrypt] Enter any natural number (this is secret key): ')
            if shift == 'Return' or shift == 'return':
                ret_flag[0] = True
                return
            try:
                shift = int(shift)
                if shift <= 0:
                    raise ValueError
            except ValueError:
                print("Secret key must be natural number!")
                print()
                input('Press Enter')
                os.system('cls' if os.name == 'nt' else 'clear')
                CLI_Caesar.print_info_about_encryption_mode()
                shift = None
                continue
        return shift

    @staticmethod
    def read_correct_filename(ret_flag):
        filename = None
        while filename is None:
            filename = input('[Caesar][Encrypt] Enter the full path to the file you want to encrypt (with extension): ')
            # Let the user exit encryption mode at any time
            # Although it looks very ugly
            if filename == 'Return' or filename == 'return':
                ret_flag[0] = True
                break
            try:
                open(filename, 'rb')
            except IOError:
                print("Can't open file. Try to enter path again.")
                print()
                input('Press Enter')
                os.system('cls' if os.name == 'nt' else 'clear')
                CLI_Caesar.print_info_about_encryption_mode()
                filename = None
                continue
        return filename

    @staticmethod
    def decrypt():
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

    @staticmethod
    def decrypt_without_shift():
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

    @staticmethod
    def encrypt_text():
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

    @staticmethod
    def decrypt_text():
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

    @staticmethod
    def decrypt_text_without_shift():
        os.system('cls' if os.name == 'nt' else 'clear')
        pass


CLI.start()
