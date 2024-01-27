# """1) Take a number from the user and print sum from 1 to that number """

# sum_upto_number = int(input("Please enter a number to sum upto"))

# cnt = 1 
# my_sum= 0  
# while(cnt <=sum_upto_number ):
#     my_sum = my_sum+cnt
#     cnt+=1
# print("The sum upto" ,sum_upto_number, "is",my_sum);

# # or 
# sum = 0 
# for i in range(1,int(input("Please enter a number"))+1):
#     sum = sum+i
# print(sum)   

"""2) Take a number from the user and print all Odd numbers from 1 to that number """

number_from_user = int(input("Please enter a number "))

current_number_being_checked = 0
while(current_number_being_checked<= number_from_user):
    if current_number_being_checked%2 !=0:
        print(current_number_being_checked,end=" ")
    current_number_being_checked+=1

# using for loop
for i in range(1,number_from_user+1,2):
    print(i , end = "--")
    
# """3) Take a number from the user and print all Even numbers from 1 to that number """

# number_from_user = int(input("Please enter a number "))

current_number_being_checked = 0
while(current_number_being_checked<= number_from_user):
    if current_number_being_checked%2 ==0:
        print(current_number_being_checked,end=" ")
    current_number_being_checked+=1

# using for loop
for i in range(0,number_from_user+1,2):
    print(i , end = "--")
