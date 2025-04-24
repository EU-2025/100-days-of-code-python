def add(num_1, num_2):
    return num_1 + num_2

def substract(num_1, num_2):
    return num_1 - num_2

def product(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

operations = {
    "+" : add,
    "-" : substract,
    "*" : product,
    "/" : division,
}
def calculation(num_1, num_2, operation):
    """Using dictionaries the operations are called from the other functions"""
    return operations[operation](num_1,num_2)


# def calculation(num_1, num_2, operation):
#     if operation == "+":
#         return adition(num_1, num_2)
#     elif operation == "-":
#         return sustraccion(num_1, num_2)
#     elif operation == "*":
#         return product(num_1, num_2)
#     elif operation == "/":
#         return division(num_1, num_2)
#     else:
#         return