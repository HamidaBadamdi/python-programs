'''
Program Name: Using Python Modules in Different Ways

Description:
This program demonstrates how to import and use functions
from a user-defined module using different import methods.

Methods Demonstrated:
1. Import entire module
2. Import specific functions from module
3. Import all functions using *
4. Import module using alias name

Module Used:
mymodule.py

Author: Hamida Badamdi

'''

# Method 1: Import Entire Module
import mymodule

a = int(input("Enter first number : "))
b = int(input("Enter first number : "))

print("\nAddition : ", mymodule.add(a , b))
print(mymodule.greet("Ruhi"))
print("\n------------------------\n")

# Method 2: Import Specific Functions
from mymodule import subtract,multi

print("Subtraction : " , mymodule.subtract(12,4))
print("Multiplication : ", mymodule.multi(8,7))
print("\n------------------------\n")

# Method 3: Import All Functions
from mymodule import *

print("Addition : " , mymodule.add(100,200))
print(mymodule.greet("Python"))
print("\n------------------------\n")

# Method 4: Import with Alias Name

import mymodule as mm

print("Addition : " ,mm.add(5,6))
print("Multiplication : ",mm.multi(6,3))






