from art import logo


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


calc_functions = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    first_num = int(input("Type first number. "))
    for i in calc_functions:
        print(i)
    math_symbol = input("What function do you want? ")
    continue_calculation = True

    while continue_calculation:
        


calculator()