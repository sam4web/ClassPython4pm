'''
# While Loop

# Syntax
# while <condition>:
#   <operation>

# While loop example
a = 0
while a < 5:
    print(a, "Hello, World!")
    a += 1

# Opposite while loop
i = 5
while i > 0:
    print(i, end=" ")
    i -= 1

# Multiplication Table
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1

# Sum of five numbers
s = i = 0
n = int(input('Enter n: '))
while i < n:
    x = int(input("Enter x: "))
    s += x
    i += 1
print('Sum:', s)

# Working with string
a = "Python"
i = 0
while i < len(a):
    print(a[i])
    i += 1

# Remove space
a = "Hello World I am Python"
i = 0
while i < len(a):
    if a[i] != " ":
        print(a[i], end="")
    i += 1


# Control statement

# break - end the loop
for i in range(5):
    if i == 3:
        break
    print(i)

a = "Hello I am Python"
for i in a:
    if i == " ":
        break
    print(i, end='')

# continue - skips code in loop
for i in range(5):
    if i == 3:
        continue
    print(i)

a = "Hello I am Python"
for i in a:
    if i == " ":
        continue
    print(i, end='')

i = 0
a = "Hello I am Python"
while i < len(a):
    if a[i] == " ":
        break
    else:
        print(a[i])
    i += 1

i = 0
a = "Hello I am Python"
while i < len(a):
    if a[i] == " ":
        i += 1
        continue
    else:
        print(a[i], end="")
    i += 1
'''

# WAP to detect if the given no. is prime or composite
num = int(input('Enter a number: '))
isComp = False
if num >= 2:
    for i in range(1, num + 1):
        if num % i == 0 and i != 1 and i != num:
            isComp = True
    if isComp:
        print('Number is composite.')
    else:
        print('Number is prime.')
else:
    print('Enter number 2 or greater than 2.')

# OR
n = int(input("Enter n: "))
for i in range(2, n):
    if n % i == 0:
        print("Num is composite.")
        break
else:
    print("Num is composite.")
