"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 5

"""
# -----------------------------------------------------------------------------------------------------------------
#Exercise 5

# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation

# # reference code 

# 	first_num = int(input("Please enter First number:"))
# 	second_num = int(input("Please enter Second number:"))
# 	returned_value = my_addition(first_num,second_num)
# 	print("The Addition of the numbers is ",returned_value)

# 	returned_value = my_square(first_num)
# 	print("The Square of the number is ",returned_value)

# 	returned_value = my_exponenation(first_num,second_num)
# 	print("The exponenation of the numbers is ",returned_value)


# calculator_program (needs to quit when the user want to quit):
# menu:
# what operation do you want to do:
# 1: Addition
# 2: Square
# 3: exponenation

# -----------------------------------------------------------------------------------------------------------------


def my_calculator(operation, num1, num2=None):
    if operation == 1:  # Addition
        return num1 + num2
    elif operation == 2:  # Square
        return num1 ** 2
    elif operation == 3:  # Exponentiation
        return num1 ** num2
    else:
        return None

# Main program
while True:
    print("Menu:")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentiation")
    print("4: Quit")

    choice = int(input("What operation do you want to perform? "))

    if choice == 4:
        print("Quitting the calculator.")
        break

    if choice in (1, 2, 3):
        num1 = float(input("Enter the first number: "))
        
        if choice == 1:
            num2 = float(input("Enter the second number: "))
        else:
            num2 = None

        result = my_calculator(choice, num1, num2)
        operation_name = "Addition" if choice == 1 else "Square" if choice == 2 else "Exponentiation"
        print(f"The {operation_name} result is {result}")
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
