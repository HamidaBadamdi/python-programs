# String Operations using Menu-Driven Program
# This program performs various operations on a string entered by the user

string=input("Enter the string: ")

while True:
    print("\n--------------------------------------------\n")
    print("\n*********MENU*********\n")
    print("1.Count No. of vowels.")
    print("2.Count length of string.")
    print("3.Reverse string.")
    print("4.Find and Replace string.")
    print("5.Check string is palindrome or not.")
    print("6.Exit.")
    
    
    print(f"String is: '{string}'")

    choice=int(input("\nEnter your choice: "))

    if choice == 1:
        cnt=0
        for char in string:
            if char in ('a' , 'e', 'i', 'o', 'u'):
                cnt+=1
        print(f"\nTotal no. of vowels in the string '{string}': {cnt}")

    elif choice == 2:
        length=0
        for i in string:
            length+=1
        print(f"Length of '{string}' is: {length}")

    elif choice == 3:
        rev_str=""
        for ch in range(len(string)-1,-1,-1):
            rev_str+=string[ch]

        print(f"\n Reverse String of '{string}' is: {rev_str}")


    elif choice == 4:
        old_str=string
        new_str=input("Enter new string/word to replace: ")
        string=string.replace(string,new_str)

        print(f"'{old_str}' successfully replaced by new string '{new_str}' ")

    elif choice == 5:
        rev_str=""
        for ch in range(len(string)-1,-1,-1):
            rev_str+=string[ch]

        if string == rev_str:
            print(f"'{string}' is palindrome string.")
        else:
            print(f"'{string}'1 (1).png")

    elif choice == 6:
        print("\nExiting...")
        break

    else:
        print("Invalid choice!")
        
        
    
