'''
Program Name: Map, Filter and Reduce using Lambda Functions

Description:
A Python program that demonstrates the use of built-in
functional programming tools such as map(), filter(),
and reduce() along with lambda functions.
The program performs operations on a list of numbers including
    -Finding the square of numbers
    -Filtering even numbers
    -Calculating the sum of all numbers.

Author: Hamida Badamdi

'''

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

print("\nOriginal List : ", numbers)

print("\n---------------- MAP ----------------")
#Square of each number
square = list(map(lambda x : x ** 2, numbers))
print("\nUsing map() - Square of numbers:\n",square)

print("\n---------------- FILTER ----------------")
# Select even numbers
even_num = list(filter(lambda x : x % 2 == 0, numbers))
print("\nUsing filter() - Even numbers:\n", even_num)

print("\n---------------- REDUCE ----------------")
# Find sum of all numbers
total = reduce(lambda a,b : a+b,numbers)
print("\nUsing reduce() - Sum of numbers:\n", total)





