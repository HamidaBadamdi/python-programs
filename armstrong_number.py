#A program to check wheather an inputted number is armstrong or not...
import sys
print("------Armstrong number------\n")

num=int(input("Enter the number: "))
orig=num
digit_len=len(str(num))
sum_val = 0

if digit_len == 1:
    print(num , "is armstrong number.")
    sys.exit()
    
while num > 0:
    digit=num % 10
    sum_val+=digit ** digit_len 
    num//=10
    
if (orig == sum_val):
    print(orig , "is armstrong number.")
else:
    print(orig , "is not armstrong number.")
