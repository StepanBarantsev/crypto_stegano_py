from helpers.exceptions import CryptoException
# Given a sequence of bytes. Add a few bits to each byte. Then we perform the operation mod 256
# Also there are some text methods


class Caesar:

    def __init__(self):
        pass

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

    def decrypt(self, encrypted_sequence, shift):
        pass

    def decrypt_without_shift(self, encrypted_sequence):
        pass

    def encrypt_text(self, text, shift):
        pass

    def decrypt_text(self, text, shift):
        pass

    def decrypt_text_without_shift(self, text):
        pass


seq = Caesar.encrypt(b'\xd1\x92\xd1\xb1\xd1\xba\xd2\x83\xd2\x8c', 42)
print(seq)