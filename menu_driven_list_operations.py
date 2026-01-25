lst=[]

while True:
    print("\n******MENU******\n")
    print("1.Creating a list")
    print("2.Display existing list")
    print("3.Sort List")
    print("4.Search List")
    print("5.Delete Element")
    print("6.Exit")

    choice=int(input("\nEnter your choice...."))
    
    if choice == 1:
        item=input("Enter item to add: ")
        lst.append(item)
        
    elif choice == 2:
        print("\nList items are....\n", lst)
        
    elif choice == 3:
        lst.sort()
        print("Sorted list...\n" , lst)
        
    elif choice == 4:
        item=input("Enter item to be search: ")
        if item in lst:
            print(item, " item found.")
        else:
            print(item, " not found!")
            
    elif choice == 5:
        item=input("Enter item to delete: ")
        if item in lst:
            lst.remove(item)
            print(item, " deleted from the list.")
        else:
            print(item, " not found in the list!")
            
    elif choice == 6:
        print("Exiting...")
        break
      
    else:
        print("Invalid choice!")
