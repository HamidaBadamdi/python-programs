'''
Program Name: File Copy Using File Handling

Description:
This Python program demonstrates how to copy the contents
of one text file into another using file handling operations.
The program reads data from a source file and writes it
into a destination file.

Author: Hamida Badamdi

'''

# Open source file in read mode
with open ("f1.txt", 'r') as file_r:
    content = file_r.read()

# Open destination file in write mode
with open("copy_file.txt", 'w') as file_w:
    file_w.write(content)

print("File copied successfully....")
    



