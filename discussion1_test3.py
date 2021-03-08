#!/usr/bin/env python3
"""This python script will ask the user to guess my favorite number (0-10)"""

# Asking the user to input their guess
userInput = input('Guess what my favorite number is: ')

# If else statement to compare user's input as an integer to my favorite number
if int(userInput) == 10:
    print('My favorite number is also 10!')
else:
    print('Cool! Your favorite number is ' + userInput + '. My favorite \
number is 10!')
