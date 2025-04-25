# 4. Fixing errors

# Code at the beginning
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}")

# It is good if a error is shown in the console to copy it to google.
# the try - except helps to catch errors or bugs and to give a new path without crashing the whole program.
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed an invalid number. Please try with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}")
