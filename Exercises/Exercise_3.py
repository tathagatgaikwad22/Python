
"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 3

"""# -----------------------------------------------------------------------------------------------------------------

# Exercises 3

# Loops and Conditionals 
# ----------------------
# # Solve the following using either while/do while loops
# 1) Take a number from the user and print sum from 1 to that number for eg: 10 o/p : 55
# 2) Take a number from the user and print all Odd numbers from 1 to that number  eg : 10 o/p 1 3 5 7 9
# 3) Take a number from the user and print all Even numbers from 1 to that number eg : 10 2 4 6 8 10
# -----------------------------------------------------------------------------------------------------------------

#1
num = int(input("Enter a number: "))
sum_of_numbers = 0
i = 1

while i <= num:
    sum_of_numbers += i
    i += 1

print(f"Sum of numbers from 1 to {num} is: {sum_of_numbers}")


#2

num = int(input("Enter a number: "))
i = 1

while i <= num:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1

print()  # Print a new line after the odd numbers


#3

num = int(input("Enter a number: "))
i = 2  # Start from 2, the first even number

while i <= num:
    print(i, end=' ')
    i += 2  # Increment by 2 to get the next even number

print()  # Print a new line after the even numbers





