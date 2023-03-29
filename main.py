MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
MONEY_WORTH = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money_type_amounts = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}
profit = 0


def resources_check(coffee_type):
    """If resources are sufficient to make coffee return True otw returns False"""
    for i in resources:
        if resources[i] < MENU[coffee_type]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def monetary_calculation(money_amounts):
    """Calculates the monetary value of inserted coins"""
    monetary_value = 0
    for i in money_amounts:
        monetary_value += money_amounts[i] * MONEY_WORTH[i]
    return monetary_value


def make_coffee(user_decision):
    """Calculate the resources that are left after the chosen coffee is made and prints the coffee"""
    for i in resources:
        resources[i] = resources[i] - MENU[user_decision]["ingredients"][i]
    print(f"Here is your {user_decision} ☕ Enjoy!")



is_finished = True
while is_finished:
    user_decide = input("What would you like? (espresso/latte/cappuccino): ")
    if user_decide == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"Money: ${profit}")
    elif user_decide == "off":
        is_finished = False
    else:
        if resources_check(user_decide):
            print("Please insert coins:")
            for i in money_type_amounts:
                money_type_amounts[i] = int(input(f"How many {i}: "))
            payment = monetary_calculation(money_type_amounts)
            if payment >= MENU[user_decide]["cost"]:
                profit += MENU[user_decide]["cost"]
                money_in_change = round((monetary_calculation(money_type_amounts) - MENU[user_decide]["cost"]), 2)
                print(f"Here is {money_in_change} in change.")
            else:
                print("Sorry that's not enough money.Money refunded.")
            make_coffee(user_decide)

# TODO: 1. Prompt user by asking What would you like? (espresso/latte/cappuccino):
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
