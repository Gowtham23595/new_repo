from art import logo

print(logo)

def add (n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

calculator_operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def recursion(num1):
    operator_calculation = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    function_name = calculator_operations[operator_calculation]
    result = function_name(num1,num2)
    print(f"{num1 } {operator_calculation} {num2} == {result}")
    flag = 1
    if flag:
        input_flag = input(f"Type 'Y' to continue calculating with {result}, or type n to exit.: ").lower()
        if input_flag == "n":
            flag = 0
            return
        else:
            recursion(result)
def calculator():
    num1 = int(input("What's the first number?: "))
    for key in calculator_operations:
        print(key)
    recursion(num1)


if __name__== "__main__":
    calculator()