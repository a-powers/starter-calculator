def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

symbol_dict = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": divide

}

def calculations():
    num1 = int(input("Type first number."))
    for i in symbol_dict:
        print(i)
    symbol = input("Type math symbol")
    num2 = int(input("Type second number"))
    calc = symbol_dict[symbol]
    
        
    
calculations()
