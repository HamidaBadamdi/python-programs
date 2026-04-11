'''
3.Write a program to make use of class method and instance method.
'''

class Student:
    
    school_name = "Brilliant  School"   # Class variable
    
    # Instance method
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    
    # Class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


# Create objects
s1 = Student("Ruhi", 85)
s2 = Student("Hasnain", 90)

# Call instance method
s1.display()
s2.display()

# Show class variable
print("School Name:", Student.school_name)

# Call class method to change school name
Student.change_school("Primary School")

# Show updated class variable
print("Updated School Name:", Student.school_name)
