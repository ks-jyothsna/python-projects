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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(drink):
    """Function checks if the resource is sufficient to make the drink.
    Returns true only when all the resources are sufficient. """
    water_remaining = resources["water"]
    milk_remaining = resources["milk"]
    coffee_remaining = resources["coffee"]

    if water_remaining < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif milk_remaining < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif coffee_remaining < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        return True

def coins_calculation(drink):
    """Calculates the total amount the user has entered and prints the change.
    Returns true if the amount is enough to proceed making coffee. """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total_amount_inserted = (0.25*quarters)+(0.1*dime)+(0.05*nickels)+(0.01*pennies)
    drink_cost = MENU[drink]["cost"]
    if total_amount_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change_return = total_amount_inserted - drink_cost
        print(f"Here is ${change_return:.2f} in change.")
        return True


def coffee_machine():
    profit = 0.0
    is_on = True
    print("Welcome to SANJYO coffee bar!!")
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml\n"
                  f"Milk: {resources['milk']}ml\n"
                  f"Coffee: {resources['coffee']}\n"
                  f"Money: ${profit:.2f}")
        elif is_resource_sufficient(choice) and coins_calculation(choice) == True:
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            cost = MENU[choice]["cost"]
            profit += cost
            print(f"Here is your {choice} ☕️. Enjoy!")

coffee_machine()
