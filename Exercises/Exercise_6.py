"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 6

"""

# --------------------------------------------------------------------------------------------------------------------------


# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user 

# for ex: 
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user

# Operations supported by our program are :
# 	1: Union
# 	2: Intersection 
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B 
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A

# --------------------------------------------------------------------------------------------------------------------------



# Initialize sets A and B with user-provided data
A = set(map(int, input("Enter elements for set A (comma-separated): ").split(',')))
B = set(map(int, input("Enter elements for set B (comma-separated): ").split(',')))

while True:
    print("Set A:", A)
    print("Set B:", B)
    print("Select an operation:")
    print("1: Union")
    print("2: Intersection")
    print("3: A - B")
    print("4: B - A")
    print("5: Check if an element is in set B")
    print("6: Display the number of elements in set A")
    print("7: Display the number of elements in set B")
    print("8: Add an element to set A")
    print("9: Add multiple elements to set A")
    print("10: Remove an element from set A")
    print("11: Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        union_result = A | B
        print("Union of sets A and B:", union_result)
    elif choice == '2':
        intersection_result = A & B
        print("Intersection of sets A and B:", intersection_result)
    elif choice == '3':
        diff_result = A - B
        print("A - B:", diff_result)
    elif choice == '4':
        diff_result = B - A
        print("B - A:", diff_result)
    elif choice == '5':
        element = int(input("Enter an element to check in set B: "))
        if element in B:
            print(f"{element} is a member of set B.")
        else:
            print(f"{element} is not a member of set B.")
    elif choice == '6':
        print("Number of elements in set A:", len(A))
    elif choice == '7':
        print("Number of elements in set B:", len(B))
    elif choice == '8':
        element = int(input("Enter an element to add to set A: "))
        A.add(element)
        print(f"{element} added to set A.")
    elif choice == '9':
        elements = set(map(int, input("Enter elements to add to set A (comma-separated): ").split(',')))
        A.update(elements)
        print(f"{elements} added to set A.")
    elif choice == '10':
        element = int(input("Enter an element to remove from set A: "))
        if element in A:
            A.remove(element)
            print(f"{element} removed from set A.")
        else:
            print(f"{element} is not in set A.")
    elif choice == '11':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-11).")
