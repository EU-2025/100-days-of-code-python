default = {
    "water" : 500,
    "coffee" : 100,
    "milk" : 300,
    "Money" : 0
}

drinks = {
    "expresso" : {
        "water" : 50,
        "coffee" : 18,
        "price" : 1.5
    },
    "latte" : {
        "water" : 200,
        "coffee" : 24,
        "milk" : 150,
        "price" : 2.5
    },
    "cappuccino" : {
        "water" : 250,
        "coffee" : 24,
        "milk" : 100,
        "price" : 3.0
    }
}

def enough_materials(request):
    if drinks[request]["water"] > default["water"]:
        return False
    if drinks[request]["coffee"] > default["coffee"]:
        return False
    if request != "expresso":
        if drinks[request]["milk"] > default["milk"]:
            return False
    return True

def update_values(request):
        if request != "expresso":
            default["milk"] -= drinks[request]["milk"]
        default["Money"] += drinks[request]["price"]
        default["water"] -= drinks[request]["water"]
        default["coffee"] -= drinks[request]["coffee"]


def make_transaction(request):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = float(quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01)
    if total >= drinks[request]["price"]:
        change = total - drinks[request]["price"]
        update_values(request)
        print(f"Here's your change $ {change:.2f}")
        print(f"Enjoy your {request}!\n")
    else:
        print("Not enough money for this transaction!")

def menu(request):
    if request in drinks:
        if enough_materials(request):
            make_transaction(request)
            
    elif request == "report":
        print(f"Water: {default['water']} ml\n"
              f"Milk: {default['milk']} ml\n"
              f"Coffee: {default['coffee']} g\n"
              f"Money: $ {default['Money']}")
    elif request == "off":
        print("The machine has turned off!")
        return False
    else:
        print("Invalid option!")
    return True


working = True

while working:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    working = menu(request)





