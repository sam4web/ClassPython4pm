'''
# Dictionary
# - Indexed
# - Ordered
# - Duplicate and multiple value
# - Mutable

# Declaration
d = {}
d = dict()
print(type(d))

# Syntax
# d = {<key> : <value>, <key> : <value>, ...}
# VALUE can be duplicated but not KEY
# KEY should be unique

a = {'a': 'Apple', 'b': 'Ball', 'c': 'Cat'}
print(a)
a['a'] = 'Ant'
print(a['a'])
print(a['b'])

a = dict()
a['a'] = 'Apple'
a['b'] = 'Ball'
a['c'] = 'Cat'
print(d)

d = dict()
n = int(input('Enter n: '))
for i in range(n):
    name = input('\nEnter name: ')
    phone = int(input('Enter phone: '))
    d[name] = phone
print(d)

# using FOR LOOP in dict
a = {'Ram': 9808667694, 'Shyam': 9808667643}
a['Hari'] = 9808998765

# DEFAULT - KEYS
for i in a:
    print(i)

# KEYS
for i in a.keys():
    print(i)

# VALUES
for i in a.values():
    print(i)

# BOTH
# a.items() - Return tuple like (<key>, <value>)
for i, j in a.items():
    print(f'{i}: {j}')

# del pop()
a = {'Ram': 9808667694, 'Shyam': 9808667643, 'Hari': 9808998765}
del a['Ram']
b = a.pop('Shyam')
print(a)
print(b)

# list inside dict
a = {'Ram': [4265224, 4263942], 'Shyam': [
    4434592, 4331528], 'Hari': [4215778, 4242674]}
print(a)

d = dict()
n = int(input('Enter n: '))
for i in range(n):
    name = input('\nEnter name: ')
    ntc_phone = int(input('Enter NTC phone: '))
    ncell_phone = int(input('Enter Ncell phone: '))
    d[name] = [ntc_phone, ncell_phone]
print(d)

# update()
a = {'Ram': [4265224, 4263942], 'Shyam': [4434592, 4331528]}
b = {'Hari': [4215778, 4242674]}
a.update(b)
print(a)
print(b)

a = {'Ram': [4265224, 4263942], 'Hari': [4215778, 4242674]}
print(a['Ram'][0])


# WAP to create the given type

d = {'Name': ['Ram', 'Shyam', 'Hari'],
     'Age': [25, 34, 23],
     'Address': ['Kathmandu', 'Bhaktapur', 'Lalitpur']
     }

n = int(input('Enter n: '))
nameList = list()
ageList = list()
addList = list()
for i in range(n):
    print(f'\nContact No. #{i+1}')
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    add = input('Enter address: ')
    nameList.append(name)
    ageList.append(age)
    addList.append(add)
d = {'Name': nameList, 'Age': ageList, 'Address': addList}
print(d)


# Practice
# Dict in List
l = [{'Name': 'Ram', 'Age': 45, 'Address': 'Kathmandu'},
     {'Name': 'Shyam', 'Age': 55, 'Address': 'Lalitpur'},
     {'Name': 'Hari', 'Age': 54, 'Address': 'Bhaktapur'}, ]

l = list()
n = int(input('Enter n: '))
for i in range(n):
    print(f'\nContact No. #{i+1}')
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    add = input('Enter address: ')
    data = {'Name': name, 'Age': age, 'Address': add}
    l.append(data)
print(l)


# Dict in Dict
d = {1: {'Name': 'Ram', 'Age': 45, 'Address': 'Kathmandu'},
     2: {'Name': 'Shyam', 'Age': 55, 'Address': 'Lalitpur'},
     3: {'Name': 'Hari', 'Age': 54, 'Address': 'Bhaktapur'}, }

d = dict()
n = int(input('Enter n: '))
for i in range(n):
    no = i + 1
    print(f'\nContact No. #{no}')
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    add = input('Enter address: ')
    data = {'Name': name, 'Age': age, 'Address': add}
    d[no] = data
print(d)
'''
