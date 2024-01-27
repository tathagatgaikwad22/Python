"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 7

"""

# ------------------------------------------------------------

# Exercise 7:

# ------------------------------------------------
# Exercise : Exceptions
# -------------------------------------------------

# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 

# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)

# 4)Create the following program named "my_exception_store" with the menu below :

# Welcome User , What would you like to do today ?
#     1) Create a postive numbered list 
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     2) Create a negative  numbered list 
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
#     3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

#     4) Check if the element is present in the list 
#     Take the Input element that you would like to search
#     and which of the above three list that he want to search element from
#     Note : raise an exception if the element is not found in the list
#     with a message "Sorry, Element could not be found"
        
#     5) Refresh the program to start with blank lists
#     6) Exit

# Handle exceptions in the script for all operations 
# and let the user continue till he chooses to exit from the program 



# ------------------------------------------------------------

positive_list = []
negative_list = []
heterogeneous_list = []

def create_positive_list():
    try:
        size = int(input("Enter the size of the positive numbered list: "))
        if size <= 0:
            raise ValueError("Size must be a positive number.")
        positive_list.clear()
        for _ in range(size):
            element = int(input("Enter a positive number: "))
            if element < 0:
                raise ValueError("Negative numbers are not allowed.")
            positive_list.append(element)
        print("Positive numbered list created:", positive_list)
    except ValueError as e:
        print(f"Error: {e}")

def create_negative_list():
    try:
        size = int(input("Enter the size of the negative numbered list: "))
        if size <= 0:
            raise ValueError("Size must be a positive number.")
        negative_list.clear()
        for _ in range(size):
            element = int(input("Enter a negative number: "))
            if element >= 0:
                raise ValueError("Positive numbers/Zero are not allowed.")
            negative_list.append(element)
        print("Negative numbered list created:", negative_list)
    except ValueError as e:
        print(f"Error: {e}")

def create_heterogeneous_list():
    try:
        size = int(input("Enter the size of the heterogeneous list: "))
        if size <= 0:
            raise ValueError("Size must be a positive number.")
        homogeneous = True
        heterogeneous_list.clear()
        for i in range(size):
            element = input(f"Enter element {i + 1}: ")
            if i > 0 and type(element) != type(heterogeneous_list[0]):
                homogeneous = False
            heterogeneous_list.append(element)
        if homogeneous:
            raise ValueError("All elements of the same datatype are not allowed.")
        print("Heterogeneous list created:", heterogeneous_list)
    except ValueError as e:
        print(f"Error: {e}")

def search_element():
    element = input("Enter the element you want to search: ")
    search_list = None
    try:
        list_choice = int(input("Enter the list to search (1 for positive, 2 for negative, 3 for heterogeneous): "))
        if list_choice == 1:
            search_list = positive_list
        elif list_choice == 2:
            search_list = negative_list
        elif list_choice == 3:
            search_list = heterogeneous_list
        else:
            raise ValueError("Invalid list choice.")
        if element not in search_list:
            raise ValueError("Element not found.")
        print(f"Element found in the list: {element}")
    except ValueError as e:
        print(f"Error: {e}")

while True:
    print("Welcome User, What would you like to do today?")
    print("1) Create a positive numbered list")
    print("2) Create a negative numbered list")
    print("3) Create a heterogeneous list")
    print("4) Check if the element is present in the list")
    print("5) Refresh the program to start with blank lists")
    print("6) Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        create_positive_list()
    elif choice == '2':
        create_negative_list()
    elif choice == '3':
        create_heterogeneous_list()
    elif choice == '4':
        search_element()
    elif choice == '5':
        positive_list.clear()
        negative_list.clear()
        heterogeneous_list.clear()
        print("Lists refreshed.")
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")
