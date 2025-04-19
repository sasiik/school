import random


class Encryptor:

    def __init__(self):
        self.nonce = random.randint(1, 1000)  # random int
        self.MAX_NORMAL_USE = 255  # only for basic latin

    def check_string_for_eligibility(self, string):
        for letter in string:
            if ord(letter) > self.MAX_NORMAL_USE:
                raise ValueError(
                    f'This symbol can not be used: {letter}. Use normal, understandable language. Only latin letters.')
        return True

    def define_encryption_key(self):
        enc_key_raw = input('Enter encryption key: ')
        self.check_string_for_eligibility(enc_key_raw)
        return enc_key_raw.strip()

    def define_text(self):
        text_raw = input('Enter a text to encrypt: ')
        self.check_string_for_eligibility(text_raw)
        return text_raw.strip()

    def encrypt_text(self, text, enc_key):
        enc_text = ''
        # logic
        for i, text_sym in enumerate(text):
            encrypted_sym = ord(
                text_sym) + ord(enc_key[i * self.nonce] if i*self.nonce < len(enc_key) else enc_key[i*self.nonce % len(enc_key)])
            enc_text += chr(encrypted_sym)
        return enc_text

    def decrypt_text(self, enc_text, enc_key):
        decrypted_text = ''
        # logic
        for i, enc_text_sym in enumerate(enc_text):
            decrypted_sym = ord(
                enc_text_sym) - ord(enc_key[i * self.nonce] if i*self.nonce < len(enc_key) else enc_key[i*self.nonce % len(enc_key)])
            decrypted_text += chr(decrypted_sym)
        return decrypted_text


if __name__ == '__main__':
    encryptor = Encryptor()
    nonce = encryptor.nonce
    enc_key = encryptor.define_encryption_key()
    text = encryptor.define_text()
    encrypted_text = encryptor.encrypt_text(text, enc_key)
    decrypted_text = encryptor.decrypt_text(encrypted_text, enc_key)
    print('Text:', text)
    print('Encryption key:', enc_key)
    print('Nonce:', nonce)
    print('Encrypted text:', encrypted_text)
    print('Decrypted text:', decrypted_text)
