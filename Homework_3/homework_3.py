# triple_quotes='''
# ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
#  ⠀⠀ ⠀    •●Welcome To Vlad's Calculator●•
# ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
# '''
# print(triple_quotes)
#
# operation = input("""ஜ We have few options: +; -; /; *. ஜ
# Choose the one you like:""")
#
#
# Operation +
# if operation == '+':
#     first_number = input("Enter first value: ")
#     if first_number.isdigit():
#         second_number = input("Second value: ")
#         if second_number.isdigit():
#             print(f"{first_number} + {second_number} = {int(first_number) + int(second_number)}")
#         else:
#             print(f"{second_number} is not digit")
#     elif first_number.isalpha():
#           second_number = input("Second value: ")
#           print(f"{first_number} + {second_number} = {first_number + second_number}")
#     else:
#         print(f"{first_number} is not digit or letter")
#
#
# Operation -
# elif operation == '-':
#     first_number = input("Enter first value: ")
#     if first_number.isdigit():
#         second_number = input("Second value: ")
#         if second_number.isdigit():
#             print(f"{first_number} - {second_number} = {int(first_number) - int(second_number)}")
#         else:
#             print(f"{second_number} is not digit")
#     else:
#         print(f"{first_number} is not digit or letter")


# Operation *
# elif operation == '*':
#     first_number = input("Enter first value: ")
#     if first_number.isdigit():
#         second_number = input("Second value: ")
#         if second_number.isdigit():
#             print(f"{first_number} * {second_number} = {int(first_number) * int(second_number)}")
#         else:
#             print(f"{second_number} is not digit")
#     else:
#         print(f"{first_number} is not digit or letter")
#
#
# Operation /
# elif operation == '/':
#     first_number = input("Enter first value: ")
#     if first_number.isdigit():
#         second_number = input("Second value: ")
#         if second_number.isdigit():
#             print(f"{first_number} / {second_number} = {int(first_number) / int(second_number)}")
#         else:
#             print(f"{second_number} is not digit")
#     else:
#         print(f"{first_number} is not digit or letter")
# elif operation == '//':
#     print("// is not developed yet'⌒' ")
# elif operation == '%':
#     print("% is not developed yet'⌒' ")
# else:
#     print('₪NOT VALID OPERATION₪')


#                                           VLAD'S NEW CALCULATOR

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


