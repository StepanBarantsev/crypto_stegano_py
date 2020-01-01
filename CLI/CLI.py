# This is command line interface
import os
from CLI_Caesar import CLI_Caesar


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



CLI.start()
