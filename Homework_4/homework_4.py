#Task 2
list= (1, 9, 10, 90, 100, 900, 1000, 9000)
index=0
summ=0
while index<len(list):
    summ+=list[index]
    index+=1
print("summ =",summ)

#Task 3
list = [False, 0, 'str', '123', 'hello', '%', 1.2, 1]
index = 0
while True:
    if index == len(list):
        break
    if type(list[index]) == str:
        index += 1
        continue
    print(type(list[index]))
    index += 1

#ДАЛІ Я ПРОСТО ДАЖЕ НЕ ЗНАЙШОВ ЯК МОЖНА ЗРОБИТИ ЧЕРЕЗ WHILE(

#Task 4
#1
list_1= [90, 68, 23, 73, 45, 9, 100]
ln = list_1[0] if list_1 else None
for index in list_1:
    if index>ln:
        ln=index
print("Largest element is: ",ln)
for index in list_1:
    if index<ln:
        ln=index
print("Minimum number:",ln)

list_2=[38, 9, 45, 4, 85, 150, 23 ]
ln = list_2[0] if list_2 else None
for index in list_2:
    if index>ln:
        ln=index
print("Largest element is: ",ln)
for index in list_2:
    if index<ln:
        ln=index
print("Minimum number:",ln)


#2
list_1= [90, 68, 23, 73, 45, 9, 100]
list_2=[38, 9, 45, 4, 85, 150, 23 ]
list_3= []
for index in list_1:
    for j in list_2:
        if index == j:
            list_3.append(index)
            break
print(list_3)







