"""Caesar's Cipher Game. Takes in a message as a string and generates the encoded or decoded form"""
from string import ascii_lowercase

LOGO = (
    """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""
    """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"""
    """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)


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
