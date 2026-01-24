'''
Program Name: Histogram Generator

Description:
This program defines a function that takes a list of integers
and prints a simple text-based histogram using asterisks (*).

Example:
Input  : [4, 9, 5]
Output :
* * * *
* * * * * * * * *
* * * * *

'''
def histogram(numbers):
    # Loop through each number in the list
    for i in numbers:
        # Print '*' i times to form histogram bars
        print('* ' * i)


# Calling the function with sample data
data = histogram([4, 9, 5])
