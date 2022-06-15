"""
# Set
# - No indexing
# - Unordered
# - No duplicate values
# - Multiple values
# - Mutable

a = {1, 2, 3, 4, 5, 6}
b = {'Apple', 'Ball', 'Cat', 'Dog'}
print(a)
print(b)
print(type(a))
print(type(b))

# a = {1, 2, 3}
# b = {4, 5, 6}
# c = a + b   # throws an error
# print(c)

# add()
a = set()
a.add(1)
a.add(2)
a.add(3)
print(a)

# update()
a = {1, 2, 3}
b = {4, 5, 6}
a.update(b)
print(a)

# remove()
a = {1, 2, 3}
b = {4, 5, 6}
a.remove(1)
print(a)

ms = {'Ram', 'Shyam', 'Nabin', 'Sabin', 'Rakesh'}
apple = {'Shyam', 'Ram', 'Bibash', 'Gita', 'Sita', 'Suman'}
print(ms.intersection(apple))       # intersection()
print(ms.union(apple))              # union()
print(ms.difference(apple))         # difference()

U = {'Sita', 'Nabin', 'Sabin', 'Rakesh',
     'Bibash', 'Shyam', 'Suman', 'Ram', 'Gita'}

unemployed = U.difference(ms.union(apple))
print(unemployed)


"""
#
