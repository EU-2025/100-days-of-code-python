import random
import my_module
import ascii_images

# Choose a random word
secret_word = random.choice(my_module.my_words)

# Save word as list
word_spelled = []
for letter in secret_word:
    word_spelled.append(letter)

word_filling = []
for i in range(len(secret_word)):
    word_filling.append("_")

# print(secret_word)
# Initial Conditios
win_game = False
total_lives = 6
print("\nWelcome to"+ ascii_images.game_title)

# Game Logic
while total_lives > 0 and win_game == False:
    print(f"Word to guess: {my_module.return_as_string(word_filling)}")
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in word_spelled:
        if guess_letter in word_filling:
            total_lives -= 1
            print(f"You've already guessed \"{guess_letter}\". You lost a life")
        else:
            print(f"Correct! \"{guess_letter}\" is in the word")
            for i in range(len(secret_word)):
                if word_spelled[i] == guess_letter:
                    word_filling[i] = guess_letter
    else:
        total_lives -= 1
        print(f"You guesed \"{guess_letter}\", that is not in the word, You lost a life.")
    print(ascii_images.stages[6-total_lives]+"\n")
    if word_spelled == word_filling:
        win_game = True
        print(f"The word was {secret_word}")
        print("Conrgatulations, You Won!")
    else:
        print(f"***********************{total_lives}/6 LIVES LEFT***********************")

if not win_game:
    print(f"The word was {secret_word}")
    print("You lost the game!")

