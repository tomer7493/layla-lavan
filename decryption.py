
class Decryption():

    @staticmethod
    def caesar_encryption(text, shift):
        """Encrypts a given text using Caesar encryption."""
        encrypted_text = ""
        for char in text:
            # Shift the character by the given number of positions    kk,,lll.
            shifted_char = chr((ord(char) + shift) % 256)
            encrypted_text += shifted_char
        return encrypted_text

    @staticmethod
    def caesar_decryption(text, shift):
        return Decryption.caesar_encryption(text, -shift)

    @staticmethod
    def code_varnam_encryption(text, key):
        """Encrypts a given text using Code Varnam encryption."""
        encrypted_text = ""
        for i in range(len(text)):
            # Get the Unicode code point of the current character and the key.
            char_code = ord(text[i])
            key_code = ord(key[i % len(key)])
            # XOR the two code points and get the resulting character.
            encrypted_char_code = char_code ^ key_code
            # Convert the resulting code point to a hexadecimal string and add it to the encrypted text.
            encrypted_char_hex = hex(encrypted_char_code)[2:].zfill(2)
            encrypted_text += encrypted_char_hex
        return encrypted_text

    @staticmethod
    def code_varnam_decryption(text, key):
        """Encrypts a given text using Code Varnam encryption."""
        new_text = b""
        for i in range(len(text)):
            a = text[i]
            b = key[i % len(key)]
            if type(a) == str or type(a) == chr:
                a = a.encode()
            if type(b) == str or type(b) == chr:
                b = b.encode()
            new_text += a ^ b
        return new_text