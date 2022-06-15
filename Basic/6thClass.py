'''
# Python Collection
# - List
# - Tuple
# - Dictionary
# - Set

# 1. List
# - Indexed
# - Ordered
# - Multiple or duplicate data
# - Mutable

# List defination
a = [1, 2, 3, 4, 5]
b = ['Apple', 'Ball', 'Cat', 'Dog']
print(a)
print(b)
# type()
print(type(a))
print(type(b))
# len()
print(len(b))
# indexed
print(b[2])
print(b[1:3])

# Concatenate
a = [1, 2, 3, 4]
b = [5, 6, 7]
c = a + b
print(c)

# list enlargement
a = ['Apple', 'Ball']
print(a * 2)

# Muitable
b = ['Apple', 'Ball', 'Cat']
b[0] = 'Ant'
print(b)

# append()
a = list()  # Empty list
a.append('Apple')
a.append('Ball')
a.append('Cat')

# Input in list
a = list()
n = int(input('Enter n: '))
for i in range(n):
    x = int(input('Enter x: '))
    a.append(x)
print(a)
print('Max value in list: ', max(a))     # max()
print('Min value in list: ', min(a))     # min()
print('Sum of no. in list: ', sum(a))    # sum()
print('Avg of no. in list: ', sum(a)/n)  # average

a.reverse()     # reverses the list
print('Reversed form: ', a)
a.sort()        # sorts the list in ascending order
print('Ascending form: ', a)
a.reverse()     # sort then reversed
print('Decending form: ', a)

# insert()
a = ['Zebra', 'Apple', 'Xray', 'Orange', 'Banana']
a.insert(1, 'Cat')
print(a)

# extend()
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)
print(a)

# Items in list
a = ['Zebra', 'Apple', 'Xray', 'Orange', 'Banana']
for i in a:
    print(i)

# del
a = ['Zebra', 'Apple', 'Xray', 'Orange', 'Banana']
del a[1]
print(a)

# index()
a = ['Zebra', 'Apple', 'Xray', 'Orange', 'Banana']
print(a.index('Orange'))

# remove()
a = ['Zebra', 'Apple', 'Xray', 'Orange', 'Banana']
a.remove('Apple')
print(a)

# pop()
a = ['Zebra', 'Apple', 'Xray', 'Orange', 'Banana']
b = a.pop()
print(a)
print(b)
'''


# WAP to detect index of a duplicate data
'''
a = ['Apple', 'Ball', 'Cat', 'Orange', 'Banana', 'Mango', 'Cat', 'Egg', 'Cat']
index = list()
for i in range(len(a)):
    item = a[i]
    for j in range(i, len(a)):
        if item == a[j] and i != j:
            if i not in index:
                index.append(i)
            if j not in index:
                index.append(j)
print(f"Duplicate item: {item}")
print(f"Their index: {index}")
'''


# WAP to remove duplicate data
'''
a = ['Apple', 'Ball', 'Cat', 'Orange', 'Banana', 'Mango', 'Cat', 'Egg', 'Cat']
timesRepeted = 0
for i in range(len(a)):
    item = a[i]
    for j in range(i, len(a)):
        if item == a[j] and i != j:
            timesRepeted += 1
for i in range(timesRepeted):
    a.remove(item)
print(a)
'''


# WAP to search any given data
'''
a = ['Apple', 'Ball', 'Cat', 'Orange', 'Banana', 'Mango', 'Egg']
search = input("Enter item name: ")
for i in range(len(a)):
    a[i] = a[i].lower()
if search in a:
    print(f"Item \"{search}\" is in list.")
else:
    print(f"Item \"{search}\" is not in list.")
'''
