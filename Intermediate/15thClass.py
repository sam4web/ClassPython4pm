"""
# Object Oriented Programming

# Syntax
# class Hello:         # class
#     <operation>

# obj =  Hello()      # object


class Hello:
    print("Hello, World!")

obj = Hello()


class Hello:
    def hello(self):
        print("Hello World")

# static method
class Hello:
    @staticmethod
    def hello():
        print("Hello World")

obj = Hello()
obj.hello()


class Cal:
    @staticmethod
    def area(l, b):
        a = l * b
        print(a)


obj = Cal()
obj.area(10, 5)
"""

# __init__()
class Cal:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def cal(self):
        a = self.l * self.b
        print(a)


l = int(input("Enter l: "))
b = int(input("Enter b: "))
obj = Cal(l, b)
obj.cal()
