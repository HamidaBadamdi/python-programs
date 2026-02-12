'''
Program Name: Banking System Using Functions

Description:
A console-based banking system that allows users to perform
basic banking operations such as Deposit, Withdraw, and
Check Balance through a menu-driven interface.

Author: Hamida Badamdi
Date: 12-Feb-2026
'''

total_bal=0  # global balance

# Function to deposit money
def deposit(amount):
    global total_bal
    total_bal+=amount
    print("Amount Deposited: " , amount)
    check_bal()
    
# Function to withdraw money
def withdraw(amount):
    global total_bal
    
    if amount > total_bal:
        print("\nInsufficient Balance!\n")
    else:
        total_bal-=amount
        print("Amount Withdrawn: " , amount)
        check_bal()
    

# Function to check balance
def check_bal():
    print("Current Balance: ", total_bal)

def banking_system():
    while True:
        print("\n-----------------------------------------------\n")
        print("\n*****Banking System*****\n")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Exit")

        choice=int(input("\nEnter choice: "))

        if choice == 1:
            amt=int(input("Enter amount to be added: "))
            deposit(amt)
        elif choice == 2:
            amt=int(input("Enter amount to be withdraw: "))
            withdraw(amt)
        elif choice == 3:
            check_bal()
        elif choice == 4:
            print("Exiting....\nThank you!")
            break
        else:
            print("Inavlalid choice!")
            
            
#calling function
banking_system()
            
            
            
            
