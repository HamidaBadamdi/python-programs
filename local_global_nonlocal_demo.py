'''
Program: Demonstration of Local, Global and Nonlocal Variables in Python

Description:
This program explains the scope and usage of variables in Python:
1. Global Variable  - Declared outside all functions and accessible everywhere.
2. Nonlocal Variable - Declared in an enclosing function and accessed using 'nonlocal'.
3. Local Variable   - Declared inside a function and accessible only within it.

Author: Hamida Badamdi

'''

#Global Variable
x = 10

def outer_function():
    #Enclosing (nonlocal) variable 
    y = 20
   
    def inner_function():
        global x # Refers to global variable
        nonlocal y # Refers to variable of outer_function
        
        #Local Variable
        z = 30
        
        print("Inside inner_function....\n")
        print("Global Variable x = ", x)
        print("Nonlocal Variable y = " , y)
        print("Local Variable z = ", z)

        #Modifying values...
        x = 100
        y = 200
        z = 300

    # Calling inner function
    inner_function()
    
    print("\nInside outer_function after inner_function() call :\n")
    print("Modified nonlocal y = " , y)
    

# Calling outer function
outer_function()
print("\nOutside all function :\n")
print("Modified global x = " , x)
    


