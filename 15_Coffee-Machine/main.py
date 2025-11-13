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
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "money" : 0
}

def is_resource_sufficient(user_choice):
    """Returns True when order can be made, False if ingredients are insufficient."""
    choice_ingredients = MENU[user_choice]["ingredients"]
    machine_ingredients = resources["ingredients"]
    for item in choice_ingredients:
        if machine_ingredients[item] < choice_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    value_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return value_inserted


def is_transaction_successful(user_choice,value_inserted):
    """Return True when the payment is accepted, or False if money is insufficient."""
    choice_cost = MENU[user_choice]["cost"]
    print(f"The cost of the drink is ${round(choice_cost,2)}.")
    print(f"The total amount inserted is ${round(value_inserted,2)}. ")
    if choice_cost <= value_inserted:
        return_amount = value_inserted - choice_cost
        print(f"Here is ${round(return_amount,2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_choice):
    """Deduct the required ingredients from the resources and add the profit."""
    for ingredient in resources["ingredients"]:
        resources["ingredients"][ingredient] -= MENU[user_choice]["ingredients"][ingredient]
    resources["money"] += MENU[choice]["cost"]
    print(f"Here is your {user_choice} ☕️. Enjoy!")


machine_on = True

while machine_on:
    print("☕️Welcome to SANJYO's coffee bar☕️!")

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f"Water: {resources["ingredients"]["water"]}ml")
        print(f"Milk: {resources["ingredients"]["milk"]}ml")
        print(f"Coffee: {resources["ingredients"]["coffee"]}g")
        print(f"Money: ${resources["money"]}")

    elif choice == "off":
        machine_on = False

    else:
        if is_resource_sufficient(choice):
            print("Nice choice!")
            amount_inserted = process_coins()
            if is_transaction_successful(choice,amount_inserted):
                make_coffee(choice)
