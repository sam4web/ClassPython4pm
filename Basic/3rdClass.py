'''
# For loop

# range() funcation
range(5)        # 0, 1, 2, 3, 4     for (int i=0; i<5; i++)
range(1, 5)     # 1, 2, 3, 4        for (int i=1; i<5; i++)
range(1, 5, 2)  # 1, 3              for (int i=1; i<5; i+2)

# For loop example
for i in range(5):
    print(i, "Hello, World!")

# Opposite for loop
for i in range(5, 1, -1):
    print(i)

# Multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# Sum of first 10 natural number
sum = 0
for i in range(1, 11):
    sum += i
    print(sum, end=" ")

# Sum of 10 number input by user
s = 0
n = int(input("Enter n: "))
for i in range(n):
    x = int(input("Enter x: "))
    s = s + x
print(s)

# Input string value
s = str()
n = int(input("Enter n: "))
for i in range(n):
    x = input("Enter x: ")
    s = s + x + "\n"
print(s)

# Input name with phone number
s = str()
n = int(input("Enter n: "))
for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone no.: ")
    s = s + name + ": " + phone + "\n"
print(s)

# Factorial
fac = 1
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    fac *= i
print(f"{num}!: {fac}")

# Working with string
a = "Python"
for i in a:
    print(i)

# Remove space
a = "Hello World I am Python"
for i in a:
    if i != " ":
        print(i, end="")

# char in string
# len() function
a = "Python"
print(a[2])
print(len(a))
for i in range(len(a)):
    print(a[i])
'''
