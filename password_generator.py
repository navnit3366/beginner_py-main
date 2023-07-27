# 1.08.2021 - 2.08.2021

import random
import string
from random import choice

letters = string.ascii_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Tell me how you would like your password to be.')
user_letters = int(input("Number of letters: \n")) 
user_symbols = int(input(f"Numebr of symbols: \n"))
user_numbers = int(input(f"Number of numbers: \n"))

# creates parts of the password and generates a password string
# this sadly took me hours to figure out, but i do know what's going on now
pass_letters = ''.join(choice(letters) for _ in range(user_letters))
pass_symbols = ''.join(choice(symbols) for _ in range(user_symbols))
pass_numbers = ''.join(choice(numbers) for _ in range(user_numbers))
password = pass_letters + pass_symbols + pass_numbers

# shuffles given parts of password
password = ''.join(random.sample(password, len(password)))

# sorts password in alphabetical order (doesn't make it upper case;
# I use 'upper()' to make all letters in a list equal to compare them
# doesn't work without it, so
sort_password = ''.join(sorted(password, key = lambda s: (s.upper(), s)))

print(f"Here is the result: {password}")
