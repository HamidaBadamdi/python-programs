'''
7.Use appropriate functions for each classWrite a program to display MRO using 
multiple inheritance. Multiple inheritance can be done as per your choice.
'''

# Base Class 1
class Student:
    
    def __init__(self, name):
        self.name = name
    
    def show_student(self):
        print("Student Name:", self.name)


# Base Class 2
class Course:
    
    def __init__(self, course):
        self.course = course
    
    def show_course(self):
        print("Course:", self.course)


# Derived Class (Multiple Inheritance)
class Result(Student, Course):
    
    def __init__(self, name, course, marks):
        Student.__init__(self, name)
        Course.__init__(self, course)
        self.marks = marks
    
    def display_result(self):
        self.show_student()
        self.show_course()
        print("Marks:", self.marks)


# Create object
r1 = Result("Joya", "Python", 85)

# Call method
r1.display_result()

# Display MRO
print("\nMRO of Result class:")
print(Result.__mro__)
