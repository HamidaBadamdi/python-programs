'''
Program Name: Find Largest Odd Number

Description:
This program allows the user to enter multiple numbers,
stores them in a list, and displays the largest odd number.
If no odd number is found, an appropriate message is displayed.

Author: Hamida Badamdi

'''

# Taking number of elements
n=int(input("Enter the total no. of elements: "))

lst_data=[]
odd_lst=[]

for i in range(n):
    num=int(input(f"Enter value of {i+1}:"))
    lst_data.append(num)
    
    if num % 2 != 0:
        odd_lst.append(num)


print("\nList data : " , lst_data)

# Checking if odd numbers exist
if len(odd_lst) > 0:
    print("\nOdd Numbers in the List : ", odd_lst)
    print("\nLargest odd number is: " , max(odd_lst))
else:
    print("Odd number not found!")
    
