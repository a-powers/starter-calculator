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
    calc_ops = True

    while still_calculating:
        ops_symbol = input("What op do you want to make?")
        second_num = int(input("What is the second number? "))
        


calculations()        