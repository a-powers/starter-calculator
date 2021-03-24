def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

calc_func = {
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division
}

def calculator():
    num1 = int(input("What is your first number? "))
    for i in calc_func:
        print(i)
    func = input("Choose a math function. ")
    continue_calculation = True

    while continue_calculation:
        num2 = int(input("What is your second number? "))
        math_function = calc_func[func]
        answer = math_function(num1, num2)
        print(answer)
        continue_calculation = False
calculator()