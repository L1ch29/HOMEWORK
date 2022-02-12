import random
# Task 1
# 1.1
# list_1 = ([random.randint(0, 10)
# for element in range(0, 10)])
# print(list_1)
# numbers= (list_1)
# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#         return list_of_unique_numbers
# print(get_unique_numbers(numbers))

# list_2 = ([random.randint(0, 10)
# for element in range(0, 10)])
# print(list_2)
# numbers= (list_2)
# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#         return list_of_unique_numbers
# print(get_unique_numbers(numbers))
#
#
# 1.2
# list_3= []
# for index in list_1:
#     for element in list_2:
#         if index == element:
#             list_3.append(index)
#             break
# print(list_3)



#Task 2
#2.1
# list= []
# index = 0
# while index < 10:
#     list.append(random.randint(0, 100))
#     index += 1
# print(list)
# index=0
# while index < len(list):
#     print(list[index])
#     index += 1


#2.2
# list_4 = ([random.randint(0, 100)
# for element in range(0, 10)])
# print(list_4)

#2.3
# index=[]
# list =([random.randint(10, 100)
#          for index in range(0,10)])
# list.append(index)
# print(list)



#Task 3
#3.1
# number = 1
# while True:
#     if number % 2 != 0:
#         number += 1
#         continue
#     print(number)
#     number += 1
#     if number == 1128275:
#         break
#
# list= []
# index = 0
# while index < 10:
#     list.append(random.randint(0, 100))
#     index += 1
# print(list)
# index=0
# while index < len(list):
#     print(list[index])
#     index += 1

list=[]
index=0
while True:
    index=(random.randint(20, 100))
    index += 1
    if index // 2 == 0 or index // 4 ==0:
        continue
    print(index)
    if index == 100:
        break




#Task 5
# password=[]
# password= input("₪Password₪ : ")
# min_number= False
#
# if len(password) > 8:
#     min_number= True
# elif min_number:
#     print(password)
# else:
#     print("Not enough numbers'⌒'")
# if len(password)>35:
#     max_number=False
#     print("Too many values'⌒'")
#
# for element in password:
#     if element.isdigit():
#         print(element)
# for element in password:
#     if element.isupper():
#         print(element)
# for element in password:
#     if element.islower():
#         print(element)
















































