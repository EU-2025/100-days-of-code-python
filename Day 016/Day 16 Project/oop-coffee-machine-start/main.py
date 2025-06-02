from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_machine = Menu()
coffee_machine = CoffeeMaker()
money_keeper = MoneyMachine()
working = True

while working:
    option = input(f"What drink do you want today?({menu_machine.get_items()}):").lower()
    if option == "off":
        print("The coffee machine has been turned off!")
        working = False
    elif option == "report":
        coffee_machine.report()
        money_keeper.report()
    else:
        drink = menu_machine.find_drink(option)
        if drink != None:
            if coffee_machine.is_resource_sufficient(drink):
                if money_keeper.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
        else:
            continue
