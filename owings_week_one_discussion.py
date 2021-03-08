"""Used to generate a random password using chars at the specified length"""
import random

password_one = ''
chars_one = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP' \
            'QRSTUVWXYZ1234567890@#$%&'
length_one = int(50)
for i in range(length_one):
    password_one += random.choice(chars_one)
print(password_one)

def password_function():
    """pw Function"""
    password = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP' \
            'QRSTUVWXYZ1234567890@#$%&'
    length = int(50)
    for _ in range(length):
        password += random.choice(chars)
    print(password)
password_function()
