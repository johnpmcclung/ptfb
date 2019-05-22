
birth_year = input('Birth year: ')
age = 2019 - int(birth_year)
print(age)

weight_in_lbs = int(input('Enter your weight in pounds: '))
weight_in_kg = weight_in_lbs / 2.2
print('Your weight in kilograms is: ' + str(int(weight_in_kg)))

course = "Python's Course for Beginners"
print(course)

course = '''
This
looks LIke
            this
huehue
'''
print(course)

course = 'Python for Beginners'
print(course[0])
print(course[0:3])

name = 'Jennifer'
print(name[1:-1])

first_name = 'John'
last_name = 'Smith'
message = first_name + ' [' + last_name + '] is a coder'
msg = f'{first_name} [{last_name}] is a coder'
print(msg)

course = 'Python for Beginners'
print('Python' in course)

print(10 / 3)

10 ** 3

x = 10
x += 3
print(x)

x = 10 + 3 * 2
x ** 3

x = (2 + 3) * 10 - 3

x = round(2.9)
print(x)

abs(-13.43021)


import math

math.ceil(2.9)

math.floor(2.9)