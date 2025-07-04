# FileNotFound
# with open("a_file.txt") as file:
#     file.read()


# KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]


# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]


# TypeError
# text = "abc"
# print(text + 5)

try: 
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["ipjiob"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"Thay key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")