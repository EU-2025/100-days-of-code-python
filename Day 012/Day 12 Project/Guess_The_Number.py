import random

title = r'''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
'''

random_number = random.randint(1,100)
total_lives = -1
guessed_number = False
print(title)
print("Welcome to the Number Guessing Game!")
# print(f"Pssst, the number is {random_number}")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
if difficulty == "hard":
    total_lives = 5
else:
    total_lives = 10
while total_lives != 0 and not guessed_number:
    print(f"You have {total_lives} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if random_number > guess:
        print("Too low")
        total_lives -= 1
        if total_lives >0:
            print("Guess Again")
        else:
            print("You've run out of guesses. Refresh the page to run again.")
    elif random_number < guess:
        print("Too High")
        total_lives -= 1
        if total_lives >0:
            print("Guess Again")
        else:
            print("You've run out of guesses. Refresh the page to run again.")
    else:
        guessed_number = True
if guessed_number:
    print(f"You got it! The answer was {random_number}.")

    



