print("-----Caculator Program-----\n")

a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))

op=input("Enter Operator (+, -, *, /, %) : ")

def add(a , b):
    return  a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

match op:
    case '+':
        print("Addition: " ,add(a,b))
    case '-':
        print("Subtraction: " , sub(a,b))
    case '*':
        print("Multiplication: " , mul(a,b))
    case '/':
        if(b == 0):
            print("Can't be division by zero!")
        else:
            print("Division: " , div(a,b))
    case '%':
        print("Modulo division: " , mod(a,b))
    case _:
        print("Invalid operator!")
        
