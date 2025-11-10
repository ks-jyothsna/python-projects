from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_chose = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operations[operation_chose](first_number,second_number)
        print(f"{first_number} {operation_chose} {second_number} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, "
                                f"or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            first_number = result
        elif choice == "n":
            os.system('cls')
            calculator()
        else:
            exit()
            
calculator()


