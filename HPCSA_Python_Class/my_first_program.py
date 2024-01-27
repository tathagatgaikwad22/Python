# # function_definitions

# def my_addition(first_num, second_num):
# 	return first_num+ second_num

# def my_square(first_num):
# 	return first_num**2

# def my_exponentiation(first_num,second_num):
# 	return first_num**second_num
	
	

# # function invocation
# import function_definitions 
# first_num = int(input("Please enter First number:"))
# second_num = int(input("Please enter Second number:"))

# print("The Addition of the numbers is ", function_definitions.my_addition(first_num,second_num) ))

# print("First number squared is  ", str(function_definitions.my_square(first_num))


# print("First number raised to number second number is  ", str(function_definitions.my_exponentiation(first_num,second_num))


# # idea
# def atm_withdrawl():
# 	1 -- validating you atm pin
# 	2 -- check your sufficient balance
# 	3 -- dispense cash
# 	4 -- optional print the receipt

# atm_withdrawl()

# def atm_withdrawl(param1,param2 = 10):
# 	1 -- validating you atm pin
# 	2 -- check your sufficient balance
# 	3 -- dispense cash
# 	4 -- optional print the receipt

# atm_withdrawl(1,2)	
# atm_withdrawl(1)	

# counter = 1
# while( counter <6 ):
# 	input("Please enter the number")
# 	counter = counter+ 1
# 	print(f"counter after increment {counter}")
 
# print(list(range(1,6,1)))
# for counter in range(1,6,1):
# 	input("Please enter the number")
# 	print(f"counter after increment {counter}")
 
# string_value = "12345" 
# for character in string_value:
#     print(character)


# d = {"new_key":100}

# # # print(d.get("new_key"))
# # # print(d.get("new_key1"))
# # print(d.get("new_key1",200))
# """
# if the key is present :
#     return the Value
# else:
#     add the key to the dictionary with the default ValueError
#     return default Value
# """
# lv_key = "new_key"
# default_value = 200

# # if lv_key in d:
# #     print(d[lv_key])
# # else:
# #     d[lv_key] = default_value
# #     print(d[lv_key])

# print(d.setdefault(lv_key,default_value)    )



# def dtype_menu():
# 	print("Available dataypes ")
# 	print("1: int \n 2: float \n 3: string \n 4: list \n 5: tuple \n 6: dictionary \n 7: set ")
# 	dtype_val=	int(input("Enter the datatype choice of the value: "))
# 	return dtype_val

# def my_dictionary():
#     d = {}
#     no_of_keys = int(input("Enter no of keys to the dictionary"))

#     for i in range(no_of_keys):
#         key = input("Enter the key: ")
#         dtype_val = dtype_menu()
        
#         if (dtype_val == 1):
#             value= input("Enter the value: ")
#             d[key] = int(value)		
#         elif (dtype_val == 2):
#             value= input("Enter the value: ")
#             d[key] = float(value)		
#         elif (dtype_val == 3):
#             value= input("Enter the value: ")
#             d[key] = value
#         elif (dtype_val == 4):
#             value= input("Enter the values comma separated: ").split(",")
#             d[key] = value
#         elif (dtype_val == 5):
#             value= tuple(input("Enter the values comma separated: ").split(","))
#             d[key] = value
#         elif (dtype_val == 6):
#              d[key] = my_dictionary()		
#         elif (dtype_val == 7):
#             value= set(input("Enter the values comma separated: ").split(","))
#             d[key] = value
#         else:
#             print("Invalid datatype encountered")
	
#     print(d.items())
#     return d
        
		
# my_dictionary()		


# # ---
# """
# {
# 'employee_id' : 1,
# 'employee_name' : 'Sarwesh'
# 'account_number' : 829389283982839,
# 'salary' : 1000.99999,
# 'address' : {'home_address' : 'Pune' , 'work_address' : 'mumbai'} ,
# 'awards': ['employeeOfTheYear','StarOfTheMonth']
# 'subjects_enrolled' : ('Physics','Chemistry')
# }
# """

# keys = ['employee_id','employee_name','account_number','salary','address','awards','subjects_enrolled']
# values = [1,'test',23,23.20,{'home_address' : 'Pune' , 'work_address' : 'mumbai'},['employeeOfTheYear','StarOfTheMonth'],('Physics','Chemistry')]
        
# d = {}
# for i in range(len(keys)):
#     d[keys[i]]= values[i]        
	
    
# my_set = { [1,2,3] }    
# print(my_set)

d= {
    1: "red" , 2: "Blue" , 3: "Orange"
}

# try:
#     #Now take the key as input from the user and print its corresponding colour 
#     print(d[int(input("Enter key"))])
# except KeyError:
#     print("Colour not found" )
    

# l = ["hello","How","Are","you","doing"]  
# try:
#     # Now take the index that the user want the data of and print the value at that location  
#     print(l[int(input("Index:"))])
# except IndexError:
#     print("Value not found")

class expiry_date(Exception):
    pass

# age = int(input("age of the user"))
# no_of_days_lived = age*365

# #Exception handle the code such that if the user has lived for more than 100001 days
# if no_of_days_lived > 100001 :
#         # raise an exception with you lived for so long , may be you will die soon:)
#         print("you lived for so long , may be you will die soon:)")
#         raise expiry_date
# else:
#     print(no_of_days_lived)    

# class negative_number_received(Exception):
#     pass

# # definition
# def  create_positive_numbered_list(my_int_list):
#     """
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     """
   
#     for i in range(int(input("No of elements:"))):
#         val = int(input("element please:")) 
#         if val >0 :
#             my_int_list.append(val)
#         else:
#             raise negative_number_received    
#     print(my_int_list)            

# # execution
# my_int_list1=[]    
# create_positive_numbered_list(my_int_list1)    



# class positive_number_received(Exception):
#     pass

# # definition
# def  create_negative_numbered_list(my_int_list):
#     """
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     """
   
#     for i in range(int(input("No of elements:"))):
#         val = int(input("element please:")) 
#         if val <0 :
#             my_int_list.append(val)
#         else:
#             raise positive_number_received
#     print(my_int_list)            

# # execution
# my_int_list1=[]    
# create_negative_numbered_list(my_int_list1)   





# # my custom exception created 
# class homogenous_list_error(Exception):
#     pass

# def value_provider(element):
#     datatype_choice = int(input(f"Please choose a datatype of the {element} to be added \
#         \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))

#     if datatype_choice == 1:
#         ret_val = int(input("Please enter an integer to be added "))
#     if datatype_choice == 2:
#         ret_val = float(input("Please enter a float to be added "))
#     if datatype_choice == 3:
#         ret_val = input("Please enter a string to be added ")
#     if datatype_choice == 4:
#         ret_val = tuple(input("Please enter a tuple to be added like 1,2 ").split(","))
#     if datatype_choice == 5:
#         ret_val = input("Please enter a list to be added like 1,2,3,4 ").split(",")
#     if datatype_choice == 6:
#         ret_val = set(input("Please enter a set to be added like 1,2 ").split(","))
#     if datatype_choice == 7:
#         my_temp_dict = {}
#         keys = input("Please enter the keys of the dictionary to be added like key1,key2 ").split(",")
#         for key in keys : 
#             my_temp_dict[key] = value_provider('key'+key)
#         ret_val = my_temp_dict
#     return ret_val

# def create_heterogenous_list(my_list):
#     """    3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
#     """
#     for cntr in range(0,int(input("Please enter number of elements to the heterogenous list"))):
#         my_list.append(value_provider('Index'+str(cntr)))
#     print(my_list)   
    
#     # check if we are have a homogenous list  
#     is_homogenous = True
#     for subscript in range(1,len(my_list)):
#         if  type(my_list[0]) != type(my_list[subscript]):
#             is_homogenous = False
#             break
        
#     if is_homogenous:
#         raise homogenous_list_error
#     else:
#         print("We received a Heterogenous list ")    
        
# my_list = []        
# create_heterogenous_list(my_list)

# import classes_objects_demo_2

# temp_var= int(input("Please enter a number"))
# print(temp_var)


# with open("my_first_file.txt","r" )  as file1:
#     temp_var= file1.read()

# with open("my_first_file_copy.txt","w" ) as file2:
#     file2.write(temp_var)

# with open("my_first_file_copy.txt","w" ) as file2:
#     with open("my_first_file.txt","r" )  as file1:
#         for line in file1:
#             file2.write(line)
    
# with open("my_first_file_copy.txt","r" ) as file1:
#     print(file1.read()    )



# import numpy as np
# np.random.rand(2)    
# *
# **
# ***
# ****
# *****
# for iteration_number in range(1,6):
#         print("*"*iteration_number)
    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for iteration_number in range(1,6):
#     for inner_number in range(1,iteration_number+1):
#         print(inner_number,end = " ")
#     print()    
# ******
# *****
# ****
# ***
# **
# *
# for iteration_number in range(6,0,-1):
#     print("*"*iteration_number)

# 1 2 3 4 5 6 
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1    
# for iteration_number in range(6,0,-1):
#     for inner_number in range(1,iteration_number+1):
#         print(inner_number,end = " ")
#     print()      

"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""    
# no_of_rows = 5
# for iteration_number in range(1,no_of_rows):
#     #space (n-iteration_number)
#     print(" "*(no_of_rows-iteration_number), end = "")
#     print("*"*(2*iteration_number-1))
"""
*********
 *******
  *****
   ***
    *
"""    
# no_of_rows = 5
# for iteration_number in range(no_of_rows,0,-1):
#     #space (n-iteration_number)
#     print(" "*(no_of_rows-iteration_number), end = "")
#     print("*"*(2*iteration_number-1))    


# A
# A B
# A B C
# A B C D
# A B C D E

# print(chr(65))
for iteration_number in range(1,6):
    for inner_number in range(1,iteration_number+1):
        print(chr(64+inner_number),end = " ")
    print()  