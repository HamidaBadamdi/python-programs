'''
Program Name: Student Operations Menu-Driven System

Description:
This Python program implements a menu-driven student management
system using a dictionary.

Each student record is stored using roll number as the key
and name and city as values.

Operations Included:
- Add Student
- Search Student
- List All Students
- Update Student Details
- Delete Student
- Exit

Concepts Used:
- Dictionary

Author: Hamida Badamdi

'''
students ={}

# Function to add student
def add_student():
    roll_no = int(input("Enter the student roll no. : "))

    if roll_no in students:
        print("\nStudent alrey exists!")
    else:
        name = input("Enter student name : ")
        city = input("Enter city :")
        students[roll_no] = {'name' : name , 'city' : city}
        print("\nstudent added scuccessfully...")


# Function to search student
def search_student():
    roll_no = int(input("Enter student roll no. to be search : "))

    if roll_no in students:
        print(f"'{roll_no}'  found....")
        print("\nName : " , students[roll_no]['name'])
        print("City  : " , students[roll_no]['city'])

    else:
        print(f"'{roll_no}' not  found!")


# Function to list all students   
def list_all_students():
    if not students:
        print("\nNo student record available!")
    else:
        print("\n --------------- All Students Records ---------------\n")
        for roll_no, data in students.items():
            print(f"Roll No. : { roll_no}, Name : {data['name'] } , City: {data['city']}\n")

# Function to update student
def update_student():
    roll_no = int(input("Enter student roll no. to update : "))

    if roll_no in students:
        update_ch =int(input("Which details you want to update ?\n1.Name\n2.City\nEnter : "))

        if update_ch == 1:
            name = input(("Enter new name : "))
            students[roll_no]['name'] =name
            print("\nstudent details updated successfully....\n ")
        elif update_ch == 2:
            city = input(("Enter new city name : "))
            students[roll_no]['city']=city
            print("\nstudent details updated successfully....\n ")
        else:
            print("\nInvalid Choice!")
        
    else:
        print(f"\n'{roll_no}' Student not found!")
        
# Function to delete student
def delete_student():
     roll_no = int(input("Enter student roll no. to delete : "))

     if roll_no in students:
         del students[roll_no]
         print("\nstudent deleted successfully....")
     else:
         print(f"\n'{roll_no}' Student not found!")

while True:
    print("\n-------------------------- STUDENT OPERATIONS MENU --------------------------\n")
    print("1. Add Student\n2.Search Student\n3.List All Students\n4.Upadate Student\n5.Delete Student\n6.Exit\n")

    choice=int(input("\nEnter your choice : "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        list_all_students()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("\nExiting....")
        break
    else:
        print("Invalid Choice!")
        
        
        
               
    
    
