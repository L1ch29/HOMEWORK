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



def welcome():
    print("""
 ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
  ⠀⠀ ⠀    •●Welcome To Vlad's Calculator●•
 ●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
 """)

def count():
    print(count)
operations = input("""
ஜWe have few optionsஜ
Choose the one you like: +, -, /, *, %, // : 
""")

first_number = int(input("Enter first value: "))
second_number = int(input("Enter second value: "))

# Operation +
if operations == '+':
    print("{} + {} = ".format(first_number, second_number ))
    print(first_number + second_number)
# Operation -
elif operations == '-':
    print("{} - {} = ".format(first_number, second_number))
    print(first_number - second_number)
# Operation *
elif operations == '*':
    print("{} * {} = ".format(first_number, second_number))
    print(first_number * second_number)
# Operation /
elif operations == '/':
    print("{} / {} = ".format(first_number, second_number))
    print(first_number / second_number)
# Operation %
elif operations == '%':
    print("{} % {} = ".format(first_number, second_number))
    print(first_number % second_number)
# Operation //
elif operations == '//':
    print("{} // {} = ".format(first_number, second_number))
    print(first_number // second_number)
# Operation **
elif operations == '**':
    print("{} ** {} = ".format(first_number, second_number))
    print(first_number ** second_number)
else:
    print('₪NOT VALID OPERATION₪')


def again():
    print(again)
count_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
if count_again.upper() == 'Y':count()
elif count_again.upper() == 'N':print('See you later.')
else:
    again()
    count()