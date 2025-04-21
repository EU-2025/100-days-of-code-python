print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \\o\\_`"-._
             .'     / /                    \\ \\     '.
             |=====/o/======================\\o\\=====|
             |____/_/________..____..________\\_\\____|
             /   _/ \\_     <_o#\\__/#o_>     _/ \\_   \\
             \_________\####################/_________/
              |===\\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \\__     '-.\\uuu/.-'    __/ \\__ |
              |==== .'.'^'.'.====|
              |  _\\o/   __  {.' __  '.} _   _\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

      ''')
print("Welcome to Treasure Island.")
print("Your misson is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go?"
                  "\n\tType \"left\" or \"right\"\n").lower()
if direction == "left":
    print("You've come to a lake.There is an island in the miffle of the lake.")
    action = input("\tType \"swim\" to swim across. Type \"wait\" for waiting for a boat\n").lower()
    if action == "wait":
        door = input("You arrive at the island unharmed."
                     "There is a house with 3 doors. One red,one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "red":
            print("There's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You've found the treasure. You Win!")
        elif door == "blue":
            print("You enter a room full of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exists. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    
 