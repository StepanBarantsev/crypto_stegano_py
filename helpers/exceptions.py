class CryptoException(Exception):
    def __init__(self, text):
        self.txt = text


class SteganoException(Exception):
    def __init__(self, text):
        self.txt = text

