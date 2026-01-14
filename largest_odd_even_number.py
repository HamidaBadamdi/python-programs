print("------Find Largest Odd Number from the inputted 10 Numbers....\n")

#1st approach using list
odd_num=[]
even_num=[]
print("Enter 10 numbers....\n")

for i in range(1,11):
    num=int(input(f"Enter value for number {i}:" , ))

    if( num % 2 != 0):
        odd_num.append(num)
    else:
        even_num.append(num)

print("\nOdd numbers : " , odd_num)
print("\nEven numbers : " , even_num)
print("--------------------------------\n")
print("Maximum odd number: " , max(odd_num))
print("\nMaximum even number: " , max(even_num))

#2nd approach using single variable....

'''print("\n-----------------------------------\n")
max_odd=None
max_even = None

for i in range (1, 11):
    num=int(input(f"Enter value for number {i}: "))
    
    if num % 2 != 0 and (max_odd == None or num > max_odd):
        max_odd=num
    elif num % 2 == 0 and (max_even == None or num > max_even):
        max_even = num
print("--------------------------------\n")        
print("Maximum odd number: " , max_odd)
print("\nMaximum even number: " , max_even)'''





        
        
