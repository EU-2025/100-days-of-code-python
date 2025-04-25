import random
import os
from game_data import data 
import art

def random_person():
    return random.choice(data)

continue_game = True
score = 0
while continue_game:
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    people_seen = []
    if len(people_seen) != 0:
        person_1 = people_seen[len(people_seen)-1]
    else:
        person_1 = random_person()
    people_seen.append(person_1)
    person_2 = random_person()
    while person_2 in people_seen:
        person_2 = random_person()
    
    print(f"Compare A: {person_1["name"]}, {person_1["description"]}, from {person_1["country"]}.")
    print(art.versus)
    print(f"Against B: {person_2["name"]}, {person_2["description"]}, from {person_2["country"]}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if person_1["follower_count"] > person_2["follower_count"]:
       continue_game = ("a" == guess)
    elif person_1["follower_count"] < person_2["follower_count"]:
        continue_game = ("b" == guess)
    else:
        break
    people_seen.append(person_2)
    os.system('cls')
    if not continue_game:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score +=1
        if score == 22:
            print("Congratulations! You have got the maximum score 😎")
            continue_game = False
