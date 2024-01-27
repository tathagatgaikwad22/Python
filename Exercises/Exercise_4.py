"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 4

"""
# ------------------------------------------------------------------------------------------------------------------------------
# # Exercise 4 : Create a dictionary like this by taking values from the user:

# {
# 'employee_id' : 1,
# 'employee_name' : 'Sarwesh'
# 'account_number' : 829389283982839,
# 'salary' : 1000.99999,
# 'address' : {'home_address' : 'Pune' , 'work_address' : 'mumbai'} ,
# 'awards': ['employeeOfTheYear','StarOfTheMonth']
# 'subjects_enrolled' : ('Physics','Chemistry')
# }
# ------------------------------------------------------------------------------------------------------------------------------


employee_id = int(input("Enter employee ID: "))
employee_name = input("Enter employee name: ")
account_number = int(input("Enter account number: "))
salary = float(input("Enter salary: "))
home_address = input("Enter home address: ")
work_address = input("Enter work address: ")
awards = input("Enter awards (comma-separated): ").split(',')
subjects_enrolled = input("Enter subjects enrolled (space-separated): ").split()

# Create the dictionary
employee_info = {
    'employee_id': employee_id,
    'employee_name': employee_name,
    'account_number': account_number,
    'salary': salary,
    'address': {
        'home_address': home_address,
        'work_address': work_address
    },
    'awards': awards,
    'subjects_enrolled': tuple(subjects_enrolled)
}

# Print the resulting dictionary
print(employee_info)
