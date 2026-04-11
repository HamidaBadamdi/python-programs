'''
4. Write a program to make use of inner class 
'''

# Outer class
class Student:
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.address = self.Address()   # Creating inner class object
    
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        self.address.display_address()
    
    # Inner class
    class Address:
        
        def __init__(self):
            self.city = "Surat"
            self.state = "Gujarat"
        
        def display_address(self):
            print("City:", self.city)
            print("State:", self.state)


# Create object of outer class
s1 = Student("Hamida", 101)

# Call method
s1.display()
