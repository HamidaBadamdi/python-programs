print("-----Generate Student Result-----\n\n")

print("Enter 4 subjects marks...")

m1=int(input("Enter Subject-1 marks: "))
m2=int(input("Enter Subject-2 marks: "))
m3=int(input("Enter Subject-3 marks: "))
m4=int(input("Enter Subject-4 marks: "))

total= m1 + m2 + m3 + m4
perc= total/4

if(perc >= 90):
    grade='A+'
elif(perc >= 80):
    grade='A'
elif(perc >= 70):
    grade='B'
elif(perc >= 60):
    grade='C'
elif(perc >= 50):
    grade='D'
else:
    grade='Fail'

print("\n-----------Result-----------\n")
print("Subject-1 : "  , m1)
print("Subject-2 : "  , m2)
print("Subject-3 : "  , m3)
print("Subject-4 : "  , m4)
print("------------------------------")
print("Total     : "  , total)
print("Percentage: "  , perc)
print("Grade     : "  , grade)



