from xml.etree.ElementTree import tostringlist

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

#option 1
# my_password = []
# pass_letters = random.sample(letters,nr_letters)
# pass_symbols = random.sample(symbols,nr_symbols)
# pass_numbers = random.sample(numbers,nr_numbers)
# my_password.extend(pass_letters+pass_symbols+pass_numbers)
# print(my_password)
# random.shuffle(my_password)
# final_password = "".join(my_password)
# print(my_password)
# print(f"Your password is: {final_password}")

# option 2
my_password = []
for i in range(nr_letters):
    my_password.append(random.choice(letters))
for i in range(nr_symbols):
    my_password.append(random.choice(symbols))
for i in range(nr_numbers):
    my_password.append(random.choice(numbers))
print(my_password)
random.shuffle(my_password)
print(my_password)

final_password = ''.join(my_password)
print(f"Your password is: {final_password}")