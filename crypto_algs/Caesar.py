from helpers.exceptions import CryptoException


class CaesarCryptoException(CryptoException):
    pass


class Caesar:

    def __init__(self):
        pass

    # Given a sequence of bytes. Add a few bits to each byte. Then we perform the operation mod 256
    @staticmethod
    def encrypt(sequence: bytes, shift: int) -> bytes:
        if type(sequence) != bytes:
            raise TypeError('Type of sequence must be bytes')
        if type(shift) != int:
            raise TypeError('Type of shift must be integer')
        # Convert to int array
        sequence = [x for x in sequence]
        new_sequence = [(element + shift) % 256 for element in sequence]
        return bytes(new_sequence)

    @staticmethod
    def decrypt(encrypted_sequence: bytes, shift: int) -> bytes:
        return Caesar.encrypt(encrypted_sequence, -shift)

    # Returns a list of possible decryption
    @staticmethod
    def decrypt_without_shift(encrypted_sequence: bytes) -> list:
        lst = []
        for i in range(256):
            lst.append(Caesar.decrypt(encrypted_sequence, i))
        return lst

    # return text in lower case
    @staticmethod
    def encrypt_text(text: str, shift: int, lang: str) -> str:
        if type(text) != str:
            raise TypeError('Text must be str type')
        if type(shift) != int:
            raise TypeError('Type of shift must be integer')
        alphabet_lower = Caesar.return_language_alphabet(lang)['lower']
        alphabet_upper = Caesar.return_language_alphabet(lang)['upper']
        ord_first_letter_lower = ord(alphabet_lower[0])
        ord_first_letter_upper = ord(alphabet_upper[0])
        new_text = ''
        for i in text:
            if i in alphabet_lower:
                new_text += chr(((ord(i) - ord_first_letter_lower + shift) % len(alphabet_lower) + ord_first_letter_lower))
            elif i in alphabet_upper:
                new_text += chr(((ord(i) - ord_first_letter_upper + shift) % len(alphabet_upper) + ord_first_letter_upper))
            else:
                new_text += i
        return new_text

    @staticmethod
    def decrypt_text(text: str, shift: int, lang: str) -> str:
        return Caesar.encrypt_text(text, -shift, lang)

    @staticmethod
    def decrypt_text_without_shift(text: str, lang: str) -> list:
        lst = []
        # There are as many capital letters as lowercase
        l = len(Caesar.return_language_alphabet(lang)['lower'])
        for i in range(l):
            lst.append(Caesar.encrypt_text(text, i, lang))
        return lst

    @staticmethod
    def return_language_alphabet(language: str) -> dict:
        # letters must be in alphabet order
        lang_dict = {"ru":
                        {
                         "lower": "абвгдежзийклмнопрстуфхцчшщъыьэюя",
                         "upper": "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                        },
                     "en":
                         {
                          "lower": "abcdefghijklmnopqrstuvwxyz",
                          "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                         }
                     }
        try:
            return lang_dict[language]
        except KeyError:
            raise CaesarCryptoException('Unsupported language. Language must be russian (ru) or english (en)')


if __name__ == '__main__':
    print(Caesar.decrypt_text_without_shift('Съешь еще этих мягких французских булок да выпей чаю же!', 'ru'))
