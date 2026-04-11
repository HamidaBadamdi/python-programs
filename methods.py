'''
1.Write a program to create a simple class with 2 methods and execute both methods , in python

'''
# Define a class
class MyClass:
    
    # Method 1
    def greet(self):
        print("Hello! Welcome to Python class example.")
    
    # Method 2
    def add_numbers(self, a, b):
        result = a + b
        print("Sum is:", result)


# Create an object of the class
obj = MyClass()

# Call both methods
obj.greet()
obj.add_numbers(10, 20)
