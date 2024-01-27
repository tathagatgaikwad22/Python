# # list comprehension
# my_answer= list("gaurav")
# print(my_answer)

# answer = []
# for elem in "gaurav":
#     answer.append(elem)
# print(answer)    

# my_list_comprehension1 = [elem for elem in "gaurav" ]   

# print(my_list_comprehension1)

# # tuple comprehension
# answer = ()
# for elem in "gaurav":
#     answer += (elem,)
# print(answer)    

# my_tuple_comprehension = tuple(elem for elem in "gaurav" )
# print(my_tuple_comprehension)

  
# # # set comprehension
# my_set_comprehension = set(elem for elem in "gaurav" )  
# print(my_set_comprehension) 

# dict comprehension
answer ={}
for elem in "gaurav":
    answer["key"+elem] = "value"+ elem
print(answer)    
    
my_dict_comprehension = dict( ("key"+elem, "value"+elem)  for elem in "gaurav" )  
my_dict_comprehension1 = { "key"+elem : "value"+ elem  for elem in "gaurav" }

print(my_dict_comprehension) 
print(my_dict_comprehension1)    
    
# generator comprehension
my_generator_comprehension = (elem for elem in "gaurav" )

# print("my_list_comprehension is " , my_list_comprehension)
# print("my_list_comprehension1 is " , my_list_comprehension1)
# print("my_tuple_comprehension is " , my_tuple_comprehension)
# print("my_set_comprehension is " , my_set_comprehension)
# print("my_dict_comprehension is " , my_dict_comprehension)
# print("my_dict_comprehension1 is " , my_dict_comprehension1)
print("my_generator_comprehension is " , my_generator_comprehension)
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")

# before walrus operator 
val = int(input ("Please enter a numeric value "))
if (val == 10 ):
    print("HI") 

# after walrus operator
if (val := int(input ("Please enter a numeric value ")) == 10 ):
    print("HI") 