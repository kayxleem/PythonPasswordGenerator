# This is a sample Python script.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")

pw_letters = int(input("How many letters will you like in your password: "))

pw_symbols = int(input("How many symbols will you like: "))

pw_number = int(input("How many numbers will you like: "))

password = []


for char in range(1, pw_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, pw_number + 1):
    random_char = random.choice(numbers)
    password += random_char

for char in range(1, pw_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

random.shuffle(password)

newpassword = ""

for char in password:
    newpassword += char

print(f"Your password is: {newpassword}")


