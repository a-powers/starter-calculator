def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def operations():

    first_num = input("What is your first number? ")
    for i in operations:
        print(i)
    ops = input("What op do you want to make?")










operations()