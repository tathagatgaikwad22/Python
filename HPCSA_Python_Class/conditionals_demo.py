# """
# # only if 
# if condition1 :
#    executes when the condition1 is true

# # if else 
# if condition1 :
#    executes when the condition1 is true
# else :
#    executes when the condition1 is false
   
# #if elif else ladder   
# if condition1 :
#    executes when the condition1 is true
# elif condition2 :
#    executes when the condition2 is true and condition1 is false
# else :
#    executes when the both condition1 and condition2 is false

# """  

# # demo

# # if 
# weather = "cold"
# if weather == "cold":
# 	print(" I am having  green tea")

# # if else
# weather = "cold"
# if weather == "cold":
# 	print(" I am having  green tea")
# else:
# 	print(" I am having  water")
 
# # if else if ladder
# weather = "cold"
# personal_preference = "Hot"
# if weather == "Sunny":
# 	print(" I am having  cold coffee")
# elif weather == "raining":
# 	print(" I am having  hot tea")
# elif weather == "cold":
# 	print(" I am having  green tea")
# else:
# 	print(" I am having  water")

# print(" Thank you !")


# # nesting the if else if ladder
# weather = "cold"
# personal_preference = "Hot"

# if weather == "Sunny":
# 	if personal_preference == "Hot":
# 		print(" I am having  Hot coffee")
# 	else:
# 		print(" I am having  cold coffee")	
# elif weather == "raining":
# 	if personal_preference == "Hot":
# 		print(" I am having  hot tea")
# 	else:
# 		print(" I am having  cold tea")
# elif weather == "cold":
# 	if personal_preference == "Hot":
# 		print(" I am having  hot green tea")
# 	else:
# 		print(" I am having  cold green tea")
# else:
# 	if personal_preference == "Hot":
# 		print(" I am having  hot water")
# 	else:
# 		print(" I am having  cold water")
	

# print(" Thank you !")
# """
# if the number is divisible by 3 print Fizz    
# if the number is divisible by 5 print Buzz
# if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

# Testcase : 
#     21 --> Fizz
#     50 --> Buzz
#     15 --> Fizz Buzz
#     22 --> Invalid Input 
# """

num = int(input("Please enter the number"))

"""
if num %5==0 and num % 3 ==0 :
    print("Fizz Buzz")
elif num%3 == 0 :
    print("Fizz")
elif num%5 == 0 :
    print("Buzz")
else:
    print("Invalid Input")
    
"""

input_num = int(input("enter number"))
if input_num%3 == 0  : 
    print("Fizz",end = " " )
    if input_num%5 == 0 : 
        print("Buzz" )
elif input_num%5 == 0 : 
        print("Buzz" )
else:
    print("Invalid Input" )


if num %5==0  :
    if num % 3 ==0 : 
        print("Fizz Buzz")
    else:
        print("Buzz")    
elif num%3 == 0 :
    print("Fizz")
else:
    print("Invalid Input")
            
