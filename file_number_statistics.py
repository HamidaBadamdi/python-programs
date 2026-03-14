'''


'''
# Open file in write mode and write content (Creates file if it doesn't exist
with open ("numbers.txt", 'w') as file_w:
    for i in range(1,11):
        file_w.write(str(i)+ " ")
        
# Open the file in read mode
with open ("numbers.txt", 'r') as file_r:

    # Read all numbers from file
    data = file_r.read()

    # Convert string numbers into list
    num = list(map(int, data.split()))
    
    print("\nNumbers in file : ",num)

    # Calculate total, maximum and minimum and display
    print("\nTotal : ", sum(num))
    print("\nMaximum Number : ", max(num))
    print("\nMinimum Number : ", min(num))
