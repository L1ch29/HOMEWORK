import random
import math
#Task 2
members_dict = {
    'Dad-Michael': {
       'Name':'Michael',
       'Age':38,
       'Sex':'male',
       'Nationality':'american',
       'Phone':'555-111-3333',
       'Profession':'director'},

    'Mum-Clara': {
       'Name':'Clara',
        'Age':30,
        'Sex':'female',
        'Nationality':'jewish',
        'Phone':'999-3333-1111',
        'Profession':'accountant'},

    'Son-Kobe': {
        'Name':'Kobe',
        'Age':9,
        'Sex':'male',
        'Nationality':'american-Jew',
        'Phone':'777-222-4444',
        'Profession':'academy student num.5'},

    'Dog-Oscar':{
         'Name':'Oscar',
         'Age':2,
         'Sex':'male',
         'Breed': 'labrador',
         'Nationality':'canadian',
    }
}
for member, member_info in members_dict.items():
     print(f"{member}:{member_info}")


#Task 3
for member in members_dict:
     print(member)


#Task 4
element_to_find= input('₪Enter value or key which u want to search₪ :')

for member, member_info in members_dict.items():
     member_info_list= list(member_info.items())
     for info_element in member_info_list:
          if element_to_find in info_element:
               print(f"{element_to_find} was found in \n{member}:{member_info}")