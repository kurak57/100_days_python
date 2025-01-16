from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        machine_is_on = False
        print("Machine Turned off")
        print("Have a nice day :)")
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order:
        drink = menu.find_drink(order)
        if drink:
            try:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
                        money_machine.profit
            except:
                print("Please insert the correct value")