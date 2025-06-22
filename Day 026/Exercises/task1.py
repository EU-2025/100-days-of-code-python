# numbers = [1, 2, 3, 4, 5]
# new_list = []

# for num in numbers:
#     new_item = num + 1
#     new_list.append(new_item)
# print(new_list)

# numbers = [1, 2, 3, 4, 5]
# new_list = [num + 1 for num in numbers]
# print(new_list)

# my_name = "Eusebio"
# letters = [letter for letter in my_name]
# print(letters)

# double_nums = [2*num for num in range(1,5)]
# print(double_nums)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name)<=4]
# print(short_names)

long_names = [name.upper() for name in names if len(name)>4]
print(long_names)