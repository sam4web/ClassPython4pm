
# Tuple
# - Indexed
# - Ordered
# - Multiple and duplicate data
# - Mutable

# defining a tuple
a = tuple()
a = (1, 2, 3, 4, 5, 6)
print(a)
print(type(a))

# concatination
a = (1, 2, 3, 4)
b = (5, 6, 7)
c = a + b

# No append(), extend(), insert()
# No del, remove(), pop()
# No update
# No sort

a = (1, 2, 3)
# a[0] = 5    # throws an error

# tuple into list
a = (1, 2, 3, 4, 5, 6)
a = list(a)
del a[0]

# list into tuple
a = tuple(a)
print(a)    # deleted a[0]

a = tuple()
b = ("Apple", )
c = ("Ball", )
a = a + b + c
print(a)

x = tuple()
n = int(input("Enter n: "))
for i in range(n):
    a = int(input("Enter a: "))
    x = x + (a, )
print(x)

a = (23, 45, 54, 64, 23)
for i in a:
    print(i)

# Yes max(), min(), sum()

a = ('Apple', 'Ball', 'Cat', 'Dog')
if 'Apple' in a:
    print('Yes')

a = 'Apple'
print(list(a))

# tuple inside tuple
a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

info = tuple()
n = int(input("Enter n: "))
for i in range(n):
    name = input("\nEnter name: ")
    age = int(input("Enter age: "))
    add = input("Enter address: ")
    data = (name, age, add)
    info = info + (data, )
print(info)

# tuple inside tuple into list inside list
a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
b = list(a)
for i in range(len(b)):
    b[i] = list(b[i])
print(b)
