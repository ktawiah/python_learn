"""Caesar's Cipher Game. Takes in a message as a string and generates the encoded or decoded form"""
from string import ascii_lowercase
from logo import LOGO


class CaesarCipher:
    """Generates encoded or decodes form of a message"""

    def __init__(self):
        self.message = input("Type your message:\n")
        self.shift = int(input("Type the shift number: \n"))
        self.alphabet = list(ascii_lowercase)

    def encode_message(self):
        """Encodes a message"""
        encoded_message_list = []
        for character in self.message.lower():
            if character not in self.alphabet:
                encoded_message_list.append(character)
            else:
                index = self.alphabet.index(character) + self.shift
                if index > len(self.alphabet) - 1:
                    new_character = self.alphabet[index - len(self.alphabet) + 1]
                    encoded_message_list.append(new_character)
                else:
                    new_character = self.alphabet[index]
                    encoded_message_list.append(new_character)

        return f"Here's the encoded result: {''.join(encoded_message_list)}"

    def decode_message(self):
        """Decodes a message"""
        decoded_message_list = []
        for character in self.message.lower():
            if character not in self.alphabet:
                decoded_message_list.append(character)
            else:
                index = self.alphabet.index(character) - self.shift
                if index < 0:
                    new_character = self.alphabet[index + len(self.alphabet) - 1]
                    decoded_message_list.append(new_character)
                else:
                    new_character = self.alphabet[index]
                    decoded_message_list.append(new_character)
        return f"Here's the decoded result: {''.join(decoded_message_list)}"


if __name__ == "__main__":
    print(LOGO)
    restart_game = "yes"
    while restart_game == "yes":
        direction = input("Type 'encode to encrypt, 'decode' to decrypt: \n")
        cipher = CaesarCipher()
        if direction == "encode":
            print(cipher.encode_message())
            restart_game = input(
                "Type 'yes' if you want to go again. Otherwise type 'no'\n"
            )
        if direction == "decode":
            print(cipher.decode_message())
            restart_game = input(
                "Type 'yes' if you want to go again. Otherwise type 'no'\n"
            )
