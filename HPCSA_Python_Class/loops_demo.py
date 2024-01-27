
# range(start, stop,step_size)
# print(list(range(2,20,3)))
# print(list(range(2,20)))
# print(list(range(4))) #print(list(range(0,4)))
# print(list(range(5,2)))
# print(list(range(5,2,-1)))


# num=1 
# while(num<10):
#      print(num, end = " ")
#      num+=1
#      break

# num=1 
# while(num<10):
#      print(num, end = " ")
#      num= num + 1
#      continue
#      num= num + 1

# num=1 
# while(num<10):
#      print(num, end = " ")
#      continue
#      num+=1



# # if i want to print 1-5 but loop for 1-9
# num=1 
# while(num<10):
#      if num<6 : 
#         print(num, end = " ")
#      num+=1



# num=1 
# while(num<10):
#      if num<6 : 
#         print("running")
#         break
#      num+=1
#      print(num, end = " ")

# ***********************************************************
# Practice problem 1 
# ***********************************************************
# Create a game for FIZZ BUZZ and keeping playing with the user untill the user chooses to skip the game

def my_fizz_buzz():
     num = int(input("Please enter the number"))
     if num %5==0 and num % 3 ==0 :
          print("Fizz Buzz")
     elif num%3 == 0 :
          print("Fizz")
     elif num%5 == 0 :
          print("Buzz")
     else:
          print("Invalid Input")

# play = True
# while(play == True):
#      my_fizz_buzz()
#      choice = int(input("Do you want to play Press 0 to skip"))
#      if choice ==0 :
#           play = False


# while(True):
#      my_fizz_buzz()
#      choice = int(input("Do you want to play Press 0 to skip"))
#      if choice ==0 :
#           break

choice = 1
while(choice !=0 ):
     my_fizz_buzz()
     choice = int(input("Do you want to play Press 0 to skip"))
