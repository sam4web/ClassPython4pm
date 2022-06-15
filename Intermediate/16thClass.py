"""
class A:            # parent class
    pass

class B(A):         # child class
    pass

obj = B()


class Info:
    def __init__(self, name, add):
        self.name = name
        self.add = add

    def info(self):
        print(self.name, self.add)


class Data(Info):
    def data(self):
        print(f"Hello world I am {self.name}. I am from {self.add}")


name = input("Enter name: ")
add = input("Enter address: ")
obj = Data()
obj.data()
obj.info()
print(obj.name)
print(obj.add)


class A:
    pass

class B(A):
    pass

class C(B):
    pass


class A:
    pass

class B:
    pass

class C(A, B):
    pass


class Info:
    def __init__(self, add):
        self.add = add

    def info(self):
        print(self.name)

class Data(Info):
    def __init__(self, name, add):
        self.name = name
        Info.__init__(self, add)

    def data(self):
        print(f"Hello world I am {self.name}. I am from {self.add}")


class Contact:
    def __init__(self, age):
        self.age = age

class Info:
    def __init__(self, add, age):
        self.add = add
        Contact.__init__(self, age)

class Data(Info):
    def __init__(self, name, add, age):
        self.name = name
        Info.__init__(self, add, age)

    def data(self):
        print(f"Hello world I am {self.name}. I am {self.age} years old. I live in {self.add}")


class Contact:
    def __init__(self, age):
        self.age = age

class Info:
    def __init__(self, add):
        self.add = add

class Data(Info):
    def __init__(self, name, add, age):
        self.name = name
        Info.__init__(self, add)
        Contact.__init__(self, age)

    def data(self):
        print(f"Hello world I am {self.name}. I am {self.age} years old. I live in {self.add}")
"""