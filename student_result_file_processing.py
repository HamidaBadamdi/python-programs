'''
Program Name: Student Result Processing Using File Handling

Description:
This Python program reads student data from a file containing
comma-separated values such as Roll Number, Name, and Marks.
It processes each student's record to calculate the total marks,
percentage, and assigns a grade based on the percentage.

Author: Hamida Badamdi

'''

with open ("stud_result.txt" , 'w') as file_w:
    file_w.write("4121,Hamida,80,91,78,85\n4068,Sana,46,36,49,70\n4096,Naznin,52,65,70,79")


def calculate_grade(perc):
    if perc >= 90:
        return "A+"
    elif perc >= 80:
        return "A"
    elif perc >= 70:
        return "B"
    elif perc >= 60:
        return "C"
    elif perc >= 50:
        return "D"
    else:
        return "F"
            
            
with open ("stud_result.txt" , 'r') as file_r:
    for line in file_r:
        
        data=line.strip().split(',')

        if len(data) != 6:
            print("Invalid record found, skipping...")
            continue

        roll_no=int(data[0])
        stud_name=data[1]
        mark1=int(data[2])
        mark2=int(data[3])
        mark3=int(data[4])
        mark4=int(data[5])

        total = mark1 + mark2 + mark3 + mark4
        perc = total/4
        grade = calculate_grade(perc)
        
        print("Roll No. :", roll_no)
        print("Name: ", stud_name)
        print("Total : ",total)
        print("Percentage : ",perc)
        print("Grade : ",grade)
        print("\n---------------------------------------\n")
    
