#Task 1
#MAX NUMBER
def max_number(number):
    ln = list[0] if list else None
    for index in number:
        if index> ln:
            ln= index
    return ln

list= [10, 20, 30, 40, 50]
list_with_max= max_number(list)
print(list_with_max)

#MIN NUMBER
def min_number(number):
    ln = list[0] if list else None
    for index in number:
        if index< ln:
            len= index
    return ln

list= [10, 20, 30, 40, 50]
list_with_min= min_number(list)
print(list_with_min)



#Task 2
dictionary={'a':29}

def custom_function( key,value,dictionary):

        return dictionary,key,value
print(custom_function('Vlad' ,13, dictionary))




#Task 3                                    VLAD'S NEW CALCULATOR

def welcome():
    return ("""
 ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
  ⠀⠀ ⠀    •●Welcome To Vlad's Calculator●•
 ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
 """)

# Operation +
def addition(x, y):
   return x + y;
# Operation -
def subtraction(x, y):
   return x - y;
# Operation *
def multiplication(x, y):
   return x * y;
# Operation /
def division(x, y):
   return x / y;
# Operation %
def result_of_division(x, y):
    return x % y
# Operation //
def integer_division(x, y):
    return x // y
# Operation **
def exponentiation(x, y):
    return x ** y

print("""
 ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
  ⠀⠀ ⠀    •●Welcome To Vlad's Calculator●•
 ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
 """)

print("ஜWe have few optionsஜ, choose the one you like: ")
print("1. Addition +")
print("2. Subtraction -")
print("3. Multiplication *")
print("4. Division /")
print("5. Result of division %")
print("6. Integer division //")
print("7. Exponentiation **")
operation = input("Enter operation(1,2,3,4,5,6,7): ")

first_number = int(input("Enter first value: "))
second_number = int(input("Enter second value: "))

# Operation +
if operation == '1':
   print(first_number, "+", second_number, "=", addition(first_number, second_number ))
# Operation -
elif operation == '2':
   print(first_number, "-", second_number, "=", subtraction(first_number, second_number ))
# Operation *
elif operation == '3':
   print(first_number, "*", second_number, "=", multiplication(first_number, second_number ))
# Operation /
elif operation == '4':
   print(first_number, "/", second_number, "=", division(first_number, second_number ))
# Operation %
elif operation == '5':
   print(first_number, "%", second_number, "=", result_of_division(first_number, second_number ))
# Operation //
elif operation == '6':
   print(first_number, "//", second_number, "=", integer_division(first_number, second_number ))
# Operation **
elif operation == '7':
   print(first_number, "**", second_number, "=", exponentiation(first_number, second_number ))

else:
    print('₪NOT VALID OPERATION₪')


