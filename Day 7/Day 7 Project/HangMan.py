import random
import my_module

# Choose a random word
secret_word = random.choice(my_module.my_words)
print(secret_word)

# Word in blanks
blanks = []
for i in range(0,len(secret_word)):
    blanks.append("_")

total_lives = 6
total_letters = 0
guesses =[]

while total_lives > 0:
    print(f"Word to guess: {my_module.print_word(blanks)}")
    guess_letter = input("Guess a letter: ").lower()
    guesses.append(guess_letter)
    if guess_letter in secret_word:
        if guesses.count(guess_letter) > 1:
            total_lives -= 1
            print(f"You've already guessed \"{guess_letter}\", total lives remaining {total_lives}")
            continue;
        print(f"You guessed \"{guess_letter}\", it's in {secret_word}")
        for letter in secret_word:
            if letter == guess_letter:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess_letter:
                        blanks[i] = guess_letter
                total_letters+=1
        if total_letters == len(secret_word):
            print("You Won!")
            break;
    else:
        print(f"You guessed \"{guess_letter}\", it's not in {secret_word}")
        total_lives -= 1
        print(f"Total of lives remaining {total_lives}")
if total_lives == 0:
    print(f"You Lost. The word was \"{secret_word}\".")
print("GameOver")
