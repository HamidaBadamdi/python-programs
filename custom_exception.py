'''
Program Name: User Defined Exception in Python

Description:
This Python program demonstrates the implementation of a
user-defined exception. A custom exception class`InsufficientBalanceError` is created to handle the situation
when a user tries to withdraw an amount greater than the available bank balance.

Exception Used:
InsufficientBalanceError – Raised when withdrawal amount exceeds the available account balance.

Author: Hamida Badamdi

'''

class InsufficientBalanceError(Exception):
    def __init__(self,message):
        self.message = message

try:
    balance = 15000
    print("\nTotal Balance : ", balance)
    withdraw = int(input("Enter withdrawal amount : "))

    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance in Account!")
    
except InsufficientBalanceError as e:
    print("\nException: ", e.message)

else:
    balance-=withdraw
    print(f"\n{withdraw} Rs/. withdrawal successfull.")
    print("Remaining Balance: ",balance)

finally:
    print("\nTransaction Completed!")

    
    

    
