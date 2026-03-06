'''
Program Name: Basic Exception Handling in Python

Description:
A Python program that demonstrates basic exception handling
using try, except, else, and finally blocks.
The program takes two numbers as input and performs division while
handling possible runtime errors such as division by zero and invalid user input.

Author: Hamida Badamdi
'''

try:
    # Taking input from user
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    result=a/b
    print("Result : ", result)

# Handles division by zero error
except ZeroDivisionError:
    print("\nError: Division by zero is not allowed!")

# Handles invalid input error
except ValueError:
    print("\nError: Please enter valid integers!")

# Executes when no error occurs
else:
    print("\nDivision successful.")

# Always execute
finally:
    print("\nProgram execution completed...")
    

