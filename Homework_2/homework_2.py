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




#Task 2
txt = '    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '
#1
x= txt.strip()
print(x)

#2
txt = 'i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone'
print(txt.count('a'))

#3
x= txt.title()
print(x)
x= txt.upper ()
print(x)

#4
x= txt.casefold()
print(x)
#5
txt = 'i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone'
print (txt.replace("super power", "tasty breakfast"))

#6
x= txt.isalpha()
print(x)


#Task 3
user_name=input("Name:")
surname= input(f"Hello {user_name}! Enter surname:")
patronymic= input(f"Please {user_name} {surname}, Enter patronymic:")
date_of_birth= input(f"{user_name} {surname} {patronymic}, Enter Date of birth:")
full_name= input(f"Hello {user_name}! Enter ПІП:")


print(''.join(word[0] for word in full_name.split(" ")).upper())
print(f"Name: {user_name}")
print(f"Surname: {surname}")
print(f"Patronymic: {patronymic}")
print(f"Date of birth: {date_of_birth}")