"""
Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.
"""

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("Choose operation: +  -  *  /")
    op = input("Enter operator: ")

    if op == '+':
        print("Result:", num1 + num2)

    elif op == '-':
        print("Result:", num1 - num2)

    elif op == '*':
        print("Result:", num1 * num2)

    elif op == '/':
        print("Result:", num1 / num2)

    else:
        print("Invalid operator")

except ValueError:
    print("Please enter integer value only")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ArithmeticError:
    print("Arithmetic error occurred")

except Exception:
    print("Something went wrong")