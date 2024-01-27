# # Introduction to functional programming 

# function definition(regular way)
def my_addition(first_num,second_num):
    """receives two numbers from the invoking application and returns addition """
    return first_num+ second_num

# imperative way 
# wrapper function that calls the regular style function
def my_calc():
    print(my_addition(1,2))

# wrapper invocation
my_calc()

# # functional way
def my_cal(function_to_invoked,function_rev_param1,function_rev_param2):
    #print(my_addition(1,2))
    print(function_to_invoked(function_rev_param1,function_rev_param2))
# my_cal(my_addition,1,2)    
my_cal(lambda first_num,second_num :  first_num+ second_num ,1,2)    


# lambda function
# lambda inputparam : return_expression
my_lamdba_add_func = lambda first_num,second_num :  first_num+ second_num

# invoking lambda function
print(my_lamdba_add_func(1,2))

# definitions 
def my_square(first_num):
    """receives two numbers from the invoking application and returns first number squared 2 """
    return str(first_num**2)

my_lambda_square_func = lambda first_num : str(first_num**2)

# invocation
print(my_square(5))
print(my_lambda_square_func(5))

# Higher order function
def my_higher_order_func (l_func,*args):
    print(f"I am higher order function with arguments {l_func, *args}")

# # functional way that atually supports multiple parameters to the inner function
def my_cal(function_to_invoked,*args):
    print(function_to_invoked(*args))

# my_addition_lambda = lambda first_num,second_num,third_num :  first_num+ second_num +third_num
def my_addition(*args):
    """receives two numbers from the invoking application and returns addition """
    sum=0
    for num in args:
        sum = sum+num
    return sum

my_cal(my_addition,1,2,3)    
    

"""
-----------------------------------------------------------------------
EXERCISE on lambda and Higher Order Functions
-----------------------------------------------------------------------
1)  Convert following functions from function_definitions.py into lambda 
    and call them 
2)  Create my calculator exercise in functional style 
"""            

# Solution:
# exercise : create my calculator exercise in functional style 
"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""
def hof(func,param1,param2= None):
    if param2 is None:
        return func(param1)
    else: 
        return func(param1,param2)
    
#from function_definitions import *
my_addition = lambda first_number,second_number : first_number+second_number
my_square = lambda first_number, second_number = None : first_number**2
my_exponenation = lambda first_number,second_number : first_number**second_number

def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_addition(first_num,second_num)
        returned_value = hof(my_addition,first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        #returned_value = my_square(first_num)
        returned_value = hof(my_square,first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_exponenation(first_num,second_num)
        returned_value = hof(my_exponenation,first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

my_calculator()    