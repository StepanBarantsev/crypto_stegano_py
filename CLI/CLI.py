# This is command line interface
import os


class CLI:

    def __init__(self):
        pass

    @staticmethod
    def start():
        command = None
        while command != 'stop':
            print('You can get help with the command: help')
            command = input('Enter command ')
            if command == 'help':
                print('List of available commands:')
                print('help -- enter this command to get a list of available commands')
            else:
                print('Unknown command')
            # Empty input so that the text is not overwritten immediately
            input('Press Enter')
            os.system('cls' if os.name == 'nt' else 'clear')


CLI.start()
