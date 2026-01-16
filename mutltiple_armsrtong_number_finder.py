#A program to find armstrong number from 10 numbers...

lst=[]
arms_num=[]
orig=0
sum_val=0

for i in range(1 , 11):
    num=int(input(f"Enter value for number {i}: "))
    lst.append(num)
    
for val in lst:
    orig=val
    #print(orig)
    digits_len=len(str(val))
    #print(digits_len)
    while(val > 0):
        digit = val % 10
        sum_val+= digit ** digits_len
        val//=10
        
    if(orig == sum_val):
        arms_num.append(orig)
   

print("\n---------Arnstrong Number---------\n")
for val in arms_num:
    print(val)
    
       
       
                  
    



