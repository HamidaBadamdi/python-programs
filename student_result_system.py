'''
Project Title : Student Result System

Description:
A menu-driven Python program to manage student results.
The system allows users to enter subject marks, calculate
percentage, and assign grades based on performance.

Author: Hamida Badamdi

'''

marks=[]
def enter_marks():
    global marks
    marks.clear()
    no=int(input("\nEnter total no. of subjects: "))
    for i in range(no):
        m=int(input(f"\nEnter marks for subject {i+1}: "))
        marks.append(m)

def calc_pecentage():
    if not marks:
        print("\nPlease, enter marks first!")
        return None
    else:
        total=0
        for i in marks:
            total+=i


    print("\nTotal = ", total)
    perc=total/len(marks)

    print("Percentage: ",round(perc,2))
            
    return perc

def assign_grade():
    perc=calc_pecentage()

    if perc is None:
        return
    if perc >= 90:
        grade='A'
    elif perc >= 75:
        grade='B'
    elif perc >= 60:
        grade='C'
    elif perc >= 40:
        grade='D'
    else:
        grade='F'

    print("Grade = ", grade)


def stud_result_system():
    while True:
        print("\n--- Student Result System ---")
        print("1. Enter Marks")
        print("2. Calculate Total & Percentage")
        print("3. Assign Grade")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            enter_marks()
        elif choice == '2':
            calc_pecentage()
        elif choice == '3':
            assign_grade()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")
            
#Calling function
stud_result_system()            



