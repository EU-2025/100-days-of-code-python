# 2. Reproduce the bug

from random import randint
dice_images = ["➀", "➁", "➂", "➃", "➄", "➅"]
# dice_num = randint(1, 6)
# As there are many cases that do not produces errors, is better to try each individual on
# dice_num = 1 #2 #3 #4 ... #6

dice_num = randint(0,5)
print(dice_images[dice_num])

