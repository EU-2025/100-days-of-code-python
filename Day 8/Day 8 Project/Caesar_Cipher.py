import resources
import functions

print(resources.title)

decision = "yes"
selection = ""
while not decision == "no":
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    print(f"Here's the {selection}ed message: {functions.encryptation(message, shift, selection)}")
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
