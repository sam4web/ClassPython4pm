"""
# public attribute
class Info:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add


# protected attribute
class Info:
    def __init__(self, name, age, add):
        self._name = name
        self._age = age
        self._add = add


# private attribute
class Info:
    def __init__(self, name, age, add):
        self.__name = name
        self.__age = age
        self.__add = add


class Info:
    def __init__(self):
        self.name = input("Enter name: ")
        self.__add = input("Enter address: ")

    def info(self):
        print(self.name, self.__add)

class Data(Info):
    def data(self):
        print(f"Hello World I am {self.name}. I am from {self.__add}")

# Access private attribute
class Info:
    def __init__(self, name, age, add):
        self.__name = name
        self.__age = age
        self.__add = add


obj = Info("Ram", 56, "Kathmandu")
print(obj._Info__name)
print(obj._Info__age)
print(obj._Info__add)


class Info:
    def __init__(self):
        self._name = input("Enter name: ")
        self.__add = input("Enter address: ")

    def info(self):
        print(self._name, self.__add)


class Data(Info):
    def data(self):
        print(f"Hello World I am {self._name}. I am from {self._Info__add}")


obj = Data()
obj.data()
print(obj.name)
obj.info()
"""
