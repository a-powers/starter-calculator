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
    num1 = int(input("Type first number. "))
    for i in calc_functions:
        print(i)
    math_symbol = input("What function do you want? ")
    continue_calculation = True

    while continue_calculation:
        num2 = int(input("Type second number. "))
        calculation = calc_functions[math_symbol]
        answer = calculation(num1, num1)
        print(answer)
        


calculator()