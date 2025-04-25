game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    # Python does not have block scoping
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy)