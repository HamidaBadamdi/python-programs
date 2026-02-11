'''
Program Name: Lambda Arithmetic Calculator

Description:
This program demonstrates the use of lambda functions
to perform basic arithmetic operations.

Author: Hamida Badamdi

'''

# Lambda functions for arithmetic operations
add = lambda x, y: x + y
sub = lambda x, y: x - y
multi = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Division by zero not allowed!"


# Taking input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
opr = input("Enter Operator (+, -, *, /): ")


# Performing operation based on operator
if opr == '+':
    result = add(x, y)

elif opr == '-':
    result = sub(x, y)

elif opr == '*':
    result = multi(x, y)

elif opr == '/':
    result = div(x, y)

else:
    result = "Invalid Operator!"

print("-------------------------------------------------------")

# Display result
print("\nResult:", result)
