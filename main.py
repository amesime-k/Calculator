#  Calculator
from art import logo
print(logo)
# Add
def add(n1,n2):
    return n1 + n2

# Substract
def substract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

operation = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide,
}
def calculator():
    num1 = float(input("What is your first number? "))
    for symbol in operation:
        print(symbol)
    yes = True
    while yes:
        operation_symbol = input('Pick an operation ')
        num2 = float(input("What is your next number? "))
        calculate_function = operation[operation_symbol]
        answer = calculate_function(num1,num2)
    
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        another_round = input(f"Type 'y' to calculate with {answer} or 'n' to restart the calculation ")
        if another_round == 'y':
            num1 = answer
        else:
            yes = False
            calculator()

calculator()
    
