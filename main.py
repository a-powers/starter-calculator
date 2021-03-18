def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

calc_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide

}

def calculator():
    num1 = int(input("What is your first number? "))
    for i in calc_dict:
        print(i)
    symbol = input("What function do you want? ")
    continue_calculation = True

    while continue_calculation:
        num2 = int(input("What is the second number? "))
        operation = calc_dict[symbol]
        answer = operation(num1, num2)
        continue_calculation = False
        print(answer)

calculator()