import random
import math
#Task 2
members_dict = {
    'Dad': {
       'Name':'Michael',
       'Age':38,
       'Sex':'male',
       'Phone':'555-111-3333',
       'Profession':'Director'},

    'Mum': {
       'Name':'Clara',
        'Age':30,
        'Sex':'female',
        'Phone':'999-333-1111',
        'Profession':'Accountant'},

    'Son': {
        'Name':'Kobe',
        'Age':9,
        'Sex':'male',
        'Phone':'777-222-4444',
        'Profession':'student'},

    'Dog':{
         'Name':'Oscar',
         'Age':2,
         'Sex':'male',
         'Breed': 'Labrador'}
}
print(len(members_dict))


#Task 3
for member, member_info in members_dict.items():
     print(f"{member}:{member_info}")

