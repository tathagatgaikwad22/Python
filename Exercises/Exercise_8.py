"""
NAME: TATHAGAT RAJU GAIKWAD
COURSE: HPCSA
PRN NO: 230940127034
ASSIGNMENT : 8

"""
# ------------------------------------------------------------
# Exercise 8

# -------------------------
# Exercise on Inheritance:
# -------------------------
# Create a base class named Employee as follows:
# Employee (
# -- class variables and methods
# 	organisation_name, 
# 	get_organisation_name(),
# 	set_organisation_name(org_name)

# -- instance variables and methods()
# emp_id,
# name,
# base_location,
# deployed_location,
# designation,
# salary ,
# get_employee_details() 	


# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	managed_employees[],
# 	perform_appraisal_for_an_employee(emp_id,percent_raise),
# 	get_manager_details(mgr_id)
# )

# Write a main method that does the following:
# create 3 objects of Employee 
# create an object of Manager_class and add the above 3 employee objects created as managed employees 
# display get_manager_details()
# for an employee do perform_appraisal_for_an_employee()



# ---------------------------------------------------------------------




class Employee:
    organisation_name = "CDAC"  # Class variable

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.salary = salary

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}"

    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    @classmethod
    def set_organisation_name(cls, org_name):
        cls.organisation_name = org_name


class Manager(Employee):
    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
        self.managed_employees = []  # List to store managed employees

    def perform_appraisal_for_an_employee(self, emp_id, percent_raise):
        for employee in self.managed_employees:
            if employee.emp_id == emp_id:
                employee.salary *= (1 + percent_raise / 100)

    def get_manager_details(self, mgr_id):
        return self.get_employee_details() + f", Managed Employees: {len(self.managed_employees)}"


def main():
    # Create three Employee objects
    emp1 = Employee(101, "Tathagat", "HQ", "Branch 1", "Staff", 50000)
    emp2 = Employee(102, "Gautam", "HQ", "Branch 2", "Manager", 70000)
    emp3 = Employee(103, "Gaurav", "HQ", "Branch 3", "Support Enggineer", 55000)

    # Create a Manager object and add the Employee objects as managed employees
    manager = Manager(201, "Omkar", "HQ", "Branch 1", "Manager", 90000)
    manager.managed_employees.extend([emp1, emp2, emp3])

    # Display manager details
    print(manager.get_manager_details(201))

    # Perform appraisal for an employee (e.g., 101) under the manager
    manager.perform_appraisal_for_an_employee(101, 10)
    print("After Appraisal:")
    for emp in manager.managed_employees:
        print(emp.get_employee_details())

if __name__ == "__main__":
    main()
