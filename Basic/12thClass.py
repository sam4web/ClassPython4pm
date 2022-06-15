"""
# Function with argument and return type
def info(name, age, add):
    data = f"Hello, I am {name}. I am from {add}. I am {age} years old."
    return data

name = input("Enter name: ")
age = int(input("Enter age: "))
add = input("Enter address: ")
print(info(name, age, add))


def language(lan="Python"):
    print(lan)

language(C)
language("C++")
language("Java")
language("C#")
language()


# Recursive function
def hello():
    print("Hello, World!")
    hello()

hello()


def cal():
    p = int(input("Enter p: "))
    t = float(input("Enter t: "))
    r = float(input("Enter r: "))
    i = (p * t * r) / 100
    print("The value of i:", i)
    x = input("Press Enter for more calculation: ")
    if x == "":
        cal()

cal()


# Math function
import math

print(math.pow(3, 2))

print(math.pi)
print(math.e)

m = 10
a = 9.8
F = m * a * (math.sin(math.pi / 2))
print(F)

print(math.sin(math.pi / 2))

print(math.tan(math.pi / 2))

print(math.factorial(5))
"""
