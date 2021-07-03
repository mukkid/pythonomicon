sitting_on_the_toilet = True
pants_are_down = True

poopin_on_the_toiler = sitting_on_the_toilet and pants_are_down

print(poopin_on_the_toiler)

if (x % 3 == 0) and (x % 5 == 0):
    ...

day = 'monday'
is_it_a_weekend = (day == 'saturday') or (day == 'sunday')
print(is_it_a_weekend)

x = False
not x

is_everyone_elses_character_bullshit = True
is_my_character_bullshit = not is_everyone_elses_character_bullshit

print(is_my_character_bullshit)

am_i_tired = True
are_there_dirty_dishes = False
are_my_parents_coming = False

do_the_dishes = are_there_dirty_dishes and (not am_i_tired or are_my_parents_coming)
print(do_the_dishes)

days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

print(days_of_the_week[4])
print(len(days_of_the_week))
days_of_the_week[69] !!!!!! error
print(days_of_the_week[-1]) !!!! last thing

first_day = days_of_the_week[0]
second_day = days_of_the_week[1]
third_day = days_of_the_week[2]

ice_cream = ['chocolate mint', 'strawberry']
# print(ice_cream)
ice_cream.append('cookies and cream')
# print(ice_cream)
ice_cream.pop()
print(ice_cream)

ice_cream = ['chocolate mint', 'strawberry', 'cookies and cream', 'vanilla']
'''
My favorite flavor is chocolate mint
My favorite flavor is strawberry
...
...
'''
index = 0
while index < len(ice_cream):
    flavor = ice_cream[index]
    print('My favorite flavor is', flavor)
    index += 1

`for` loop
for flavor in ice_cream:
    print('My favorite flavor is', flavor)

command = ''
while command != 'quit':
    command = input('what is your command: ')
    if command == 'wake up':
        print('wake up!')
    elif command == 'make tea':
        print("here's your tea!")
    else:
        print("sorry I don't know that command")
