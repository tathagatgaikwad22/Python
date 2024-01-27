# def  my_addition():
# 	first_num = int(input("Please enter First number:"))
# 	second_num = int(input("Please enter Second number:"))
# 	print("The Addition of the numbers is ", str(first_num+ second_num))


# return_val = my_addition() 
# print("The returned value is ", return_val)

#---------------------------
def  my_addition(first_num = 100,second_num=200):
	return first_num+ second_num


first_num = int(input("Please enter First number:"))
second_num = int(input("Please enter Second number:"))

return_val = my_addition(first_num,second_num)
print("The addition is ", return_val)

# return_val = my_addition()
print("The addition is ", return_val)

