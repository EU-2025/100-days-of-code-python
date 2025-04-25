import os
import visual_resources
import functions as f
def play_game():
    game_over = False

    start_game = input("Do you want to play blackjack? Type 'y' or 'n': ")
    if start_game == 'y':
        os.system("cls")
        while not game_over:
            computer_deck = []
            user_deck = []
            print(visual_resources.logo)
            # Baraja inicial:
            print("Your cards:")
            while f.sum_deck(user_deck) > 21 or f.sum_deck(user_deck) <= 0:
                user_deck = []
                for i in range(2):
                    user_deck.append(f.random_card())
            f.print_cards_side_by_side(user_deck)
            print(f"Your current score: {f.sum_deck(user_deck)}\n")
            print("Computer cards:")
            computer_deck.append(f.random_card())
            f.print_cards_side_by_side(computer_deck)
            print(f"Computer's current score: {f.sum_deck(computer_deck)}\n")
            while f.sum_deck(user_deck) < 17 or len(user_deck) == 2 and f.sum_deck(user_deck) != 21:
                more_cards = input("Do you want on more card? Type 'y' to get one more or 'n' to pass. \n")
                if more_cards == 'y':
                    user_deck.append(f.random_card())
                    if f.sum_deck(user_deck) < 17:
                        print("Your cards:")
                        f.print_cards_side_by_side(user_deck)
                        print(f"Your current score: {f.sum_deck(user_deck)}\n")
                        print("Computer cards:")
                        f.print_cards_side_by_side(computer_deck)
                        print(f"Computer's current score: {f.sum_deck(computer_deck)}\n")
                else:
                    break
            while f.sum_deck(user_deck) <= 21 and (f.sum_deck(user_deck) >= f.sum_deck(computer_deck)):
                computer_deck.append(f.random_card())
            print("Your final deck: ")
            f.print_cards_side_by_side(user_deck)
            print(f"Your final score: {f.sum_deck(user_deck)}\n")
            print("Computer's final deck: ")
            f.print_cards_side_by_side(computer_deck)
            print(f"Computer's final score: {f.sum_deck(computer_deck)}\n")
            if f.sum_deck(user_deck) > 21:
                print("You lose. You went over 21 😭")
            else:
                if f.sum_deck(user_deck) == f.sum_deck(computer_deck):
                    print("It's a Draw. Both got the same points 😐")
                elif f.sum_deck(user_deck) == 21:
                    print("You Won. You got Exactly 21 points 😎")
                elif f.sum_deck(computer_deck) <21 and  f.sum_deck(computer_deck) > f.sum_deck(user_deck):
                    print("You lose. Your opponent was closer to 21 😑")
                else:
                    print("You Won. Your opponent excced 21 points 😂")
            game_over = ('n' == input("Do you want to play blackjack again? Type 'y' or 'n': "))
            if not game_over:
                os.system("cls")
            else:
                print("\n Thanks For Playing!")
    else:
        print("")


play_game()