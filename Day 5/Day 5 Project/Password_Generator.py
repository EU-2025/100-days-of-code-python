import random

# Lista con el abecedario: primero en minúsculas, luego en mayúsculas
letters = [ 
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters wilud you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for item in range(0,nr_letters):
    password_list.append(random.choice(letters))

for item in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for item in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for element in password_list:
    password += element

print(f"Your password is: {password}")
