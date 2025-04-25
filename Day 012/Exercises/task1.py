# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()

# print(f"enemies outside function: {enemies}")


# Global Scope
player_health = 10

def drink_potion():
    # Local Scope
    potion_strenght = 2
    print(player_health)

# print(potion_strenght)

print(player_health)

