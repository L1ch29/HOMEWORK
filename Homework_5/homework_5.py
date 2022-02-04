import random
#Task 1
#1.1
list_1 = ([random.randint(0, 10)
for element in range(0, 10)])
print(list_1)
numbers= (list_1)
def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))

list_2 = ([random.randint(0, 10)
for element in range(0, 10)])
print(list_2)
numbers= (list_2)
def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))


#1.2
list_3= []
for index in list_1:
    for j in list_2:
        if index == j:
            list_3.append(index)
            break
print(list_3)



#Task 2
#2.1
list= []
index = 0
while index < 10:
    list.append(random.randint(0, 100))
    index += 1
print(list)
while index < len(list):
    print(list[index])
    index += 1

#Task 5











