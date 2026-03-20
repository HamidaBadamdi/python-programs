'''
Program Name: Zip and Unzip Files in Python

Description:
This Python program demonstrates how to compress (zip) and
extract (unzip) files using two different approaches:
1. zipfile module
2. shutil module

Author: Hamida Badamdi

'''

import zipfile
import shutil

# -------------------- USING ZIPFILE MODULE --------------------

# Create a zip file and add a file into it
with zipfile.ZipFile('my_zip_file.zip', 'w') as zip_file:
    # Add file to zip (make sure this file exists)
    zip_file.write('stud_result.txt')

print("File zipped successfully using zipfile module...")

# Extract (unzip) the zip file
with zipfile.ZipFile('my_zip_file.zip', 'r') as zip_file:
    # Extract all files to current directory
    zip_file.extractall()

print("File unzipped successfully using zipfile module...\n")


# -------------------- USING SHUTIL MODULE --------------------

# Create a zip archive (compress entire folder or files)
# Here, it will zip current directory or specified folder
shutil.make_archive('my_files', 'zip', '.')  
print("File zipped successfully using shutil module...")

# Extract (unzip) the archive
shutil.unpack_archive('my_files.zip')
print("File unzipped successfully using shutil module...")
