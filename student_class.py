'''
Write a program to create a class for student with RollNo, Name, Age, Gender
and methods named AddStudent() and DisplayStudent()
'''

# Define Student class
class Student:
    
    # Method to add student details
    def AddStudent(self):
        self.roll_no = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")
    
    # Method to display student details
    def DisplayStudent(self):
        print("\n--- Student Details ---")
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Create object of Student class
s1 = Student()

# Call methods
s1.AddStudent()
s1.DisplayStudent()
