# 1. Describe the error
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#   The for loop is iterating in the values from the range() function that go from 1 to 19
# 2. When is the function meant to print "You got it"?
#   The function is supposed to print it when the variable i recieves the value 20
# 3. What are your assumptions about the value of i?
#   The code assumes that the varible i can get asigned the value of 20, which cannot happen