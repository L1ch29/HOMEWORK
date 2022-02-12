#Task 1
#MAX NUMBER
def max_number(number):
    ln = list[0] if list else None
    for index in number:
        if index> ln:
            ln=index
    return ln

list = [10, 20, 30, 40, 50]
list_with_max= max_number(list)
print(list_with_max)

#MIN NUMBER
def min_number(number):
    ln = list[0] if list else None
    for index in number:
        if index< ln:
            len=index
    return ln

list = [10, 20, 30, 40, 50]
list_with_min= min_number(list)
print(list_with_min)




