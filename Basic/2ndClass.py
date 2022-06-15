'''
# User input
# input function returns string
# type casting (string -> int)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = a + b
print(c)

p = int(input("Enter p: "))
t = float(input("Enter t: "))
r = float(input("Enter r: "))
i = (p * t * r) / 100
print("The value of i: ", i)

name = input("Enter name: ")
age = int(input("Enter age: "))
add = input("Enter addresss: ")
info = "Hello I am " + name + ". I am from " + add + ". I am " + str(age) + "."
print(info)


# Multiple value assign
a = 10, 20
a, b = 10, 20


# Condition
# if-else
# if <condition>:
#     <operation>
# elif <condition>:
#     <operation>
#     ...
# else:
#     <operation>


# Comparision operator
# <, >, >=, <=, ==, !=

a = int(input("Enter a number: "))
if a % 2 == 0:
    print(a, " is even.")
else:
    print(a, " is odd.")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    print(a, " is greater.")
elif b > a:
    print(b, " is greater.")
else:
    print("Both are equal.")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
o = input("Enter + - * /: ")
if o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/':
    print(a / b)
else:
    print("Invalid operator.")


# Logical operator
# and, or
a = int(input("Enter a number: "))
if (a % 2 == 0) and (a > 10):
    print("The value if even and greater then 10.")
else:
    print("Error.")

a = int(input("Enter a number: "))
if (a % 2 == 0) or (a > 10):
    print("The value if even or greater then 10.")
else:
    print("Error.")


# Nested if-else
# if < condition >:
#     if < condition >:
#         <operation >
#     else:
#         <operation >
# else:
#     <operation>

a = int(input("Enter a number: "))
if (a % 2 == 0):
    if (a > 10):
        print("The value if even and greater then 10.")
    else:
        print("The value if even but not greater than 10.")
else:
    print("Error.")
'''
