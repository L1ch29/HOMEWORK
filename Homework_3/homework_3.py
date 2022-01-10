#Task 1
x = '10'
y = '5'
z = '20'
print(f'{y}<{x}<{z}')
print(f'{x}>{y}<{z}')
print(f'{z}>{x}>{y}')
print(f'{z}>{y}<{x}')
print(f'{y}!= {x}!= {z}')
print(f'{x}<{z}>{y}')
#answer
5<10<20
10>5<20
20>10>5
20>5<10
5!= 10!= 20
10<20>5
True

#Task 3
user_name=input("Name:")
surname= input(f"Hello {user_name}! Enter surname:")
patronymic= input(f"Please {user_name} {surname}, Enter patronymic:")
date_of_birth= input(f"{user_name} {surname} {patronymic}, Enter Date of birth:")
full_name= input(f"Hello {user_name}! Enter Full name:")
print(f"Full name: {full_name}")
print(f"Name: {user_name}")
print(f"Surname: {surname}")
print(f"Patronymic: {patronymic}")
print(f"Date of birth: {date_of_birth}")

