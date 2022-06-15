'''
# List inside list

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(a)
print(type(a))
print(a[0][2])

a = [['Ram', 23, 'Kathmandu'], ['Shyam', 34, 'Bhaktapur'], ['Hari', 56, 'Lalitpur']]
search = input('Enter search value: ')
for i in a:
    if search in i:
        print(i)

a[0][0] = 'Ramesh'
print(a)

a = [['Shyam', 34, 'Bhaktapur'], ['Hari', 23, 'Lalitpur']]
a.append(['Ram', 41, 'Kathmandu'])
print(a)


# WAP to create a list inside list
data = list()
n = int(input('Enter n: '))
for i in range(n):
    name = input('\nEnter name: ')
    age = int(input('Enter age: '))
    add = input('Enter add: ')
    info = [name, age, add]
    data.append(info)
print(data)


# WAP to create a matrix with given row and column
matrix = list()
r = int(input("Enter r: "))
c = int(input("Enter c: "))
for i in range(r):
    y = list()
    for j in range(c):
        x = int(input("Enter x: "))
        y.append(x)
    matrix.append(y)
print(matrix)

'''
