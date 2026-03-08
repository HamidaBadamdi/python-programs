'''
Program Name: Arithmetic Exception Logging in Python

Description:
This Python program demonstrates how to generate and handle
an arithmetic exception (division by zero) and log the
exception details into a system log file using the logging module.
 If a division by zero occurs, the ZeroDivisionError exception is caught and recorded in a log file named "error_log.txt".

Exception Used:
ZeroDivisionError – Occurs when a number is divided by zero.

Module Used:
logging – Used to record exception details in a log file.

Author: Hamida Badamdi

'''
import logging

# Configure logging system
logging.basicConfig(
    filename = "error_log.txt",
    level = logging.ERROR,
    format = "%(asctime)s - %(levelname)s - %(message)s"
    )


try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    result = a/b  # Arithmetic Exception (division by zero)
    print("Result : ", result)

except ZeroDivisionError as e:
    print("Arithmaric Exception Occured!")

    # Logging exception into system file
    logging.error("Exception Occurred: %s", e)

finally:
    print("\nPrgram execution completed!")
    

