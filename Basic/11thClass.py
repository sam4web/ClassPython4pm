"""
# Function syntax
# def <fn_name>():
#     <operation>
# <fn_name>()


def hello():    # function define
    print('Hello, World!')
hello()         # function call


def cal():
    l = int(input('Enter l: '))     # local variable
    b = int(input('Enter b: '))     # local variable
    a = l * b
    print(a)


l = int(input('Enter l: '))     # global variable
b = int(input('Enter b: '))     # global variable
def cal():
    a = l * b
    print(a)


def cal():
    global l, b
    l = int(input('Enter l: '))
    b = int(input('Enter b: '))
    a = l * b
    print(a)

# Argument and return type
def hello(x):           # parameter
    print(x)
hello('Hello, World!')  # argument

# function with argument
def area(l, b):
    a = l * b
    print(a)

l = int(input('Enter l: '))
b = int(input('Enter b: '))
area(l, b)


def cal(a, b, o):
    if firstNum != 0 and secondNum != 0:
        if o == '+':
            print(a + b)
        elif o == '-':
            print(a - b)
        elif o == '*':
            print(a * b)
        elif o == '/':
            print(a / b)
        else:
            print('Invalid operator.')
    else:
        print('Zero is invalid.')

firstNum = int(input('Enter first number: '))
secondNum = int(input('Enter second number: '))
o = input('Enter + - * /: ')
cal(firstNum, secondNum, o)


# List in function
def info(l):
    data = f'Hello World I am {l[0]}. I am from {l[2]}. I am {l[1]} years old.'
    print(data)

name = input('Enter name: ')
age = int(input('Enter age: '))
add = input('Enter address: ')
l = [name, age, add]
info(l)

# Dict in function
def info(d):
    data = f"Hello World I am {d['Name']}. I am from {d['Address']}. I am {d['Age']} years old."
    print(data)

name = input("Enter name: ")
age = int(input("Enter age: "))
add = input("Enter address: ")
d = {"Name": name, "Age": age, "Address": add}
info(d)

# Return type function
def hello():
    return "Hello "

x = hello()
print(x + "World!")

def cal():
    l = int(input("Enter l: "))
    b = int(input("Enter b: "))
    a = l * b
    return a

area = cal()
h = int(input("Enter h: "))
v = area * h
print("The volume:", v)
"""
