import functions
import visual_resources
import os

print(visual_resources.logo)

result = 0
answer = "n"

while not answer == "":
    if answer == "n":
        number_1 = float(input("What's the first number: "))
    else:
        number_1 = result
    operation = input("+\n-\n*\n-\nChoose an operation: ")
    number_2 = float(input("What's the second number: "))

    result = functions.calculation(number_1, number_2, operation)
    print(f"{number_1} {operation} {number_2} = {result}")
    answer = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ")
    if answer == "n":
        os.system('cls')
        print(visual_resources.logo)



