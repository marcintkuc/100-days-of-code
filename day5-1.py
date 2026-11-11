import random

symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = [letter.upper() for letter in letters_small]
letters = letters_small + capital_letters

print("Welcome to the PyPassword Generator!")
symbols_count = int(input("How many special characters would you like in your password? "))
numbers_count = int(input("How many numbers would you like in your password? "))
letters_count = int(input("How many letters would you like in your password? "))

password = list()

for i in range(0,symbols_count):
    password.append(random.choice(symbols))
for i in range(0,numbers_count):
    password.append(random.choice(numbers))
for i in range(0,letters_count):
    password.append(random.choice(letters))

random.shuffle(password)
password = ''.join(password)
print(f"Your password is: {password}")