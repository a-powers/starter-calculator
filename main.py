def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculations():

    first_num = int(input("What is your first number? "))
    for i in operation:
        print(i)
    ops = input("What op do you want to make?")
    calc_ops = True

    while still_calculating:
        