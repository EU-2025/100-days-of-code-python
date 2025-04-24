import resources

def encryptation(message, shift, selection):
    actual_shift = shift
    message_encrypted = ""
    while actual_shift >25:
        actual_shift -=26
        
    for letter in message.lower():
        if letter in resources.alphabet:
            ubication = resources.alphabet.index(letter)
            if selection == "encode":
                ubication += actual_shift
                if ubication > 25:
                    ubication -= 26
            else:
                ubication -= actual_shift
                if ubication < 0:
                    ubication += 26
            message_encrypted += resources.alphabet[ubication]
    return message_encrypted

