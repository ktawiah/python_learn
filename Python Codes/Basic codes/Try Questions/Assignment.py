import threading
import re

class Valid_Email:
    def __init__(self, email_address):
        self.email_address = email_address

    def get_input(self):
        self.email_address = input('Enter email address: ')

    def valid_email(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        while not re.match(email_regex, self.email_address):
            self.email_address = input('Enter a correct email address: ')
        print(f'{self.email_address} is a valid email address')


# Create and start a thread for the valid_email method
thread = threading.Thread(target=Valid_Email('').valid_email)
thread.start()