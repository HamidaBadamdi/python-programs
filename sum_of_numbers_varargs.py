'''
Program Name: Sum of Numbers Using Variable Length Arguments

Description:
This program defines a function that accepts any number of
arguments using *args and calculates the total (sum) of all
numbers.

Date: 11-Feb-2026
'''


# Function to calculate sum of any number of arguments
def total_sum(*args):
    total = 0
    for num in args:
        total += num
        
    print("Numbers are: ",list(args))
    print("\nTotal = ", total)

total_sum(10,20,30,40,50)
