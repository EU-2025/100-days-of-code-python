import selection
import random

selection = [selection.rock, selection.paper, selection.scissors]

your_turn = int(input("What do you choose? "
                  + "Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_turn >= 0 and your_turn <= 2:
    print(selection[your_turn])

    computer_turn = random.randint(0,2)
    print(f"Computer chose:\n{selection[computer_turn]}")

    if your_turn == computer_turn:
        print("Its a Draw")
    elif (your_turn - computer_turn == 1) or (your_turn - computer_turn == -2):
        print("You Win!")
    else:
        print("You Lose.")
else:
    print("You choose a wrong number.")
