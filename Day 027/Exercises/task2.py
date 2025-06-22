# def add (*args):
#     sum = 0
#     for n in args:
#         sum+= n
#     return sum

# print(add(3, 5, 7, 18, 20))

def calculate(num, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    num += kwargs["add"]
    num *= kwargs["multiply"]
    print(num)
    
calculate(2, add=3, multiply=5)