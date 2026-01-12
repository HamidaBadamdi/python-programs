#A program to find even or odd number given by user input

print("-----Find even or odd number-----")
num=int(input("Enter the number : "))

#1st aproach using '%' operator...
if(num % 2 == 0):
    print(num , "is even number.")
else:
    print(num , "is odd number.")

#2nd approach using (/ , *)...
'''
if((num // 2) * 2 == num):
     print(num , "is even number.")
else:
    print(num , "is odd number.")'''

#3rd approach using bitwise AND (&)...
'''e.g.,
  7->   0111
  1->  &0001
       ------
       0001
'''

'''if(num & 1):
      print(num , "is odd number.")
else:
    print(num , "is even number.")'''

#4th approach...

'print(num, "is even number." if not(num % 2) else "is odd number.")'



  
     


