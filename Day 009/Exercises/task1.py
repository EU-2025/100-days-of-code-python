programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from runnung as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])
programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}


# Wipe dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Buy"] = "A moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


