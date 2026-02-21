'''
Program Name: Find Largest of Three Numbers

Description:
This Python program defines a function that accepts three numbers
as parameters and returns the largest number among them.

Author: Hamida Badamdi

'''

# Function to find largest number
def max_num(a,b,c):
    if a > b and a >c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        print(f"{a} = {b} = {c}.")

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))

# Calling function
largest=max_num(n1,n2,n3)

print(f"\nNumbers are: {n1},{n2},{n3}")
print("\nLargest Number = ", largest)


