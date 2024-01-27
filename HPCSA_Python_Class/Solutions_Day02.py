"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""

from function_definitions import *
def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_addition(first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        returned_value = my_square(first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_exponenation(first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

def iterative_calculator():
    while(True):
        print("Lets start   !!!! ")
        my_calculator()	
        choice = input("\n Do you want to continue (Y/N)").lower()     
        if choice == 'n':
            break

iterative_calculator()     