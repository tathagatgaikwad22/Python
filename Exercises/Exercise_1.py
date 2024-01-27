
"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 1

"""
# ------------------------------------------------------------------------------------------------------------------
# Exercise 1 : Questions based on variable, statements , input and print functions and operators 
# ------------------

# 1) Accept two numbers from the user and print 
# a) addition 
# b) first number squared 2 
# c) first number raised to number second number

# 2) Accept String from user and output upper case of the input string 

# 3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console

# 4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches

# 5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees

# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
# -----------------------------------------------------------------------------------------------------------------

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
square = num1 ** 2
power = num1 ** num2

print("a) Addition:", addition)
print("b) First number squared:", square)
print("c) First number raised to the second number:", power)

# Task 2
input_string = input("Enter a string: ")
uppercase_string = input_string.upper()
print("Uppercase string:", uppercase_string)

# Task 3
raise_salary_percentage = float(input("Enter the salary raise percentage: "))
name = 'gaurav'
existing_salary = 900
incremented_salary = existing_salary + (existing_salary * (raise_salary_percentage / 100))

print(f"New salary for {name} is {incremented_salary} INR")

# Task 4
height_in_cm = float(input("Enter your height in centimeters: "))
height_in_feet = height_in_cm / 30.48
feet = int(height_in_feet)
inches = (height_in_feet - feet) * 12

print(f"Your height is {feet} feet and {inches} inches")

# Task 5
dollars = float(input("Enter the number of dollars: "))
rupees = dollars * 82
print(f"{dollars} dollars is equal to {rupees} INR")

# Task 6
source = input("Enter the source: ")
destination = input("Enter the destination: ")
fare_inr = float(input("Enter the fare in INR: "))
discount_rate = float(input("Enter the discount rate percentage: "))
discounted_fare = fare_inr - (fare_inr * (discount_rate / 100))

print(f"Fare from {source} to {destination} is {fare_inr} INR with a discount of {discount_rate}%")
print(f"Discounted fare: {discounted_fare} INR")
