'''
Program Name: File Reading and Word Count in Python

Description:
This Python program demonstrates basic file handling operations.
The program first writes sample text into a file and then reads the file contents.
It displays the content of the file and calculates the total number of words present in the file.

Author: Hamida Badamdi

'''

# Open the file in write mode and write content (creates file if it doesn't exist)
with open ("myfile.txt", 'w') as file_w: 
    file_w.write("Python is a powerful programming language.\nIt is easy to learn and widely used.")
    print("Content written successfully...\n")

# Open the file in read mode
with open ("myfile.txt", 'r') as file_r:

    # Read file contents
    content=file_r.read()

    # Display file contents
    print("\n ----------------------File Content ----------------------\n")
    print(content)

# Count words
words=content.split()
print("\nTotal number of words in file: ", len(words))




    
