class CLI_Helper:

    def __init__(self):
        pass

    @staticmethod
    def read_correct_shift(ret_flag, text, mode, abstract_class):
        shift = None
        while shift is None:
            shift = input(text)
            if shift == 'Return' or shift == 'return':
                ret_flag[0] = True
                return
            try:
                shift = int(shift)
                if shift <= 0:
                    raise ValueError
            except ValueError:
                print("Secret key must be natural number!")
                abstract_class.clear_screen_and_print_info_about_mode(mode)
                shift = None
                continue
        return shift

    @staticmethod
    def read_correct_filename(ret_flag, text, mode, abstract_class):
        filename = None
        while filename is None:
            filename = input(text)
            # Let the user exit encryption mode at any time
            # Although it looks very ugly
            if filename == 'Return' or filename == 'return':
                ret_flag[0] = True
                break
            try:
                open(filename, 'rb')
            except IOError:
                print()
                print("Can't open file. Try to enter path again.")
                abstract_class.clear_screen_and_print_info_about_mode(mode)
                filename = None
                continue

            # Check that there are no dots in the file name
            split_by_dot = os.path.basename(filename).split('.')
            if len(split_by_dot) != 2:
                print()
                print('There should be no dots in the file name! Or maybe the file has several extensions.')
                abstract_class.clear_screen_and_print_info_about_mode(mode)
                filename = None

        return filename

    @staticmethod
    def read_correct_lang(ret_flag, text, mode, abstract_class):
        lang = None
        while lang is None:
            lang = input(text)
            if lang == 'Return' or lang == 'return':
                ret_flag[0] = True
                return
            if lang != 'ru' and lang != 'en':
                print()
                print("This is unsupported lang!")
                abstract_class.clear_screen_and_print_info_about_mode(mode)
                lang = None
                continue
        return lang