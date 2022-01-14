triple_quotes=''' 
●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
 ⠀⠀ ⠀    •●Welcome To Vlad's Calculator●•
●▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬●
'''
print(triple_quotes)

operation = input("""ஜ We have few options: +; -; /; *. ஜ
Choose the one you like:""")

#Operation +
if operation == '+':
    first_number = input("Enter first value: ")
    if first_number.isdigit():
        second_number = input("Second value: ")
        if second_number.isdigit():
            print(f"{first_number} + {second_number} = {int(first_number) + int(second_number)}")
        else:
            print(f"{second_number} is not digit")
    elif first_number.isdigit():
        second_number = input("Second value: ")
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    else:
        print(f"{first_number} is not digit or letter")


#Operation -
if operation == '-':
    first_number = input("Enter first value: ")
    if first_number.isdigit():
        second_number = input("Second value: ")
        if second_number.isdigit():
            print(f"{first_number} - {second_number} = {int(first_number) - int(second_number)}")
        else:
            print(f"{second_number} is not digit")
    elif first_number.isdigit():
        second_number = input("Second value: ")
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    else:
        print(f"{first_number} is not digit or letter")


#Operation *
if operation == '*':
    first_number = input("Enter first value: ")
    if first_number.isdigit():
        second_number = input("Second value: ")
        if second_number.isdigit():
            print(f"{first_number} * {second_number} = {int(first_number) * int(second_number)}")
        else:
            print(f"{second_number} is not digit")
    elif first_number.isdigit():
        second_number = input("Second value: ")
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    else:
        print(f"{first_number} is not digit or letter")


#Operation /
if operation == '/':
    first_number = input("Enter first value: ")
    if first_number.isdigit():
        second_number = input("Second value: ")
        if second_number.isdigit():
            print(f"{first_number} / {second_number} = {int(first_number) / int(second_number)}")
        else:
            print(f"{second_number} is not digit")
    elif first_number.isdigit():
        second_number = input("Second value: ")
        print(f"{first_number} / {second_number} = {first_number / second_number}")
    else:
        print(f"{first_number} is not digit or letter")



elif operation == '//':
    print("// is not developed yet'⌒' ")

elif operation == '%':
    print("% is not developed yet'⌒' ")






