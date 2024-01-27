"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 2

"""
# -----------------------------------------------------------------------------------------------------------------
# Assignment/Exercises : 2
# Topics covered : Modules,Functions,Looping,Conditional constructs,Input,Output,Collections :
# -----------------------------------------------------------------------------------------------------------------

# 1) Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user 
# for ex: ["Pratiksha","Kevin","Sachin","Yuvraj","Sania"] is provided by the user 

# Operations supported by our program are :
#   1:  Display number of elements in the members list
#   2:  Add an element to the members collection like 'Sehwag' 
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection 
#   6:  Display third, fourth and fifth element from the collection 

# Keep asking the user for the operation in this store untill he chooses to exit from the program

# Initialize the members list with the user-provided data
# --------------------------------------------------------------------------------------------------------------


members = ["Pratiksha", "Kevin", "Sachin", "Yuvraj", "Sania"]

while True:
    print("Members List:", members)
    print("Select an operation:")
    print("1: Display the number of elements in the members list")
    print("2: Add an element to the members collection")
    print("3: Add elements to the members collection")
    print("4: Remove a member from the collection at a given subscript")
    print("5: Remove the last member from the collection")
    print("6: Display the third, fourth, and fifth elements from the collection")
    print("7: Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Number of elements in the members list:", len(members))
    elif choice == '2':
        element = input("Enter the element to add: ")
        members.append(element)
        print(f"{element} added to the members list.")
    elif choice == '3':
        elements = input("Enter elements to add (comma-separated): ").split(',')
        members.extend(elements)
        print(f"{elements} added to the members list.")
    elif choice == '4':
        index = int(input("Enter the subscript to remove: "))
        if 0 <= index < len(members):
            removed_element = members.pop(index)
            print(f"Removed {removed_element} from the members list.")
        else:
            print("Invalid subscript.")
    elif choice == '5':
        if members:
            removed_element = members.pop()
            print(f"Removed the last member ({removed_element}) from the members list.")
        else:
            print("The members list is empty.")
    elif choice == '6':
        if len(members) >= 5:
            print(f"Third element: {members[2]}")
            print(f"Fourth element: {members[3]}")
            print(f"Fifth element: {members[4]}")
        else:
            print("There are not enough elements in the list to display the third, fourth, and fifth elements.")
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-7).")
