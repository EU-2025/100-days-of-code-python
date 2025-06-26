# age : int
# name : str
# height : float
# is_human : bool


# age = 12
# age = "twelve" # Generates error, its type is determined before

def police_check(age:int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    
    return can_drive

if police_check(20):
    print("You may pass")
else:
    print("Pay a fine.")


