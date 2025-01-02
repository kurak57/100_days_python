MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#My Solution
def sufficient_resources(drink):
    drink_ing = MENU[drink]["ingredients"]

    for resource in resources:
        if resource in drink_ing:
            if resources[resource] < drink_ing[resource]:
                print(f"Sorry there is not enough {resource}")
                return False
    return True

def process_coin():
    coins = ["quarter", "dimes","nickles","pennies"]
    coins_value = 0
    for coin in coins:
        try:
            input_coin = int(input(f"How many {coin}?: "))
            if coin == "quarter":
                coins_value += (input_coin * 0.25)
            if coin == "dimes":
                coins_value += (input_coin * 0.1)
            if coin == "nickles":
                coins_value += (input_coin * 0.05)
            if coin == "pennies":
                coins_value += (input_coin * 0.01)
        except ValueError:
            # print(f"Invalid Input, {coin} will not be counted.")
            pass
    print(f"Your money: ${round(coins_value,2)}")
    return coins_value

def is_transaction_succes(drink):
    drink_price = MENU[drink]["cost"]
    customer_money = process_coin()
    income = 0
    if customer_money == drink_price:
        income = drink_price
        return True
    elif customer_money > drink_price:
        print(f"Here is your change ${round(customer_money-drink_price,2)}.")
        income = drink_price
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded is ${customer_money}.")
        return False

def make_coffe(drink):
    drink_ing = MENU[drink]["ingredients"]

    for resource in resources:
        if resource in drink_ing:
            resources[resource] -= drink_ing[resource]
    print(f"Here is your {drink} ☕︎. Enjoy ☺")
money = 0

# off = True
off = False

while not off:
    order = input("what would you like! (espresso/latte/cappuccino): ").lower()
    #Secret order
    
    if order == "off":
        print("\n"*20)
        off = True
    elif order == "report":
        for resource in resources:
            print(f"{resource.title()}: {resources[resource]}")
        print(f"Money: ${money}")
    
    if order in MENU:
        if sufficient_resources(order):
            succes = is_transaction_succes(order)
            if succes:
                money += MENU[order]["cost"]
                make_coffe(order)   

# #Bootcamp Solution
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
