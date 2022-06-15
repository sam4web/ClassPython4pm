import datetime
import os

"""
# normal list
a = []
for i in range(1, 6):
    a.append(i)
print(a)

# list comprehension
a = [i for i in range(1, 6)]
print(a)

# print even number using list comprehension
a = [i for i in range(1, 21) if i % 2 == 0]
print(a)

a = ["Apple", "Ball", "Cat", "Dog", "Fish", "cat", "bat", "rat"]
b = []
for i in a:
    if i[0].isupper():
        b.append(i)
print(b)

a = ["Apple", "Ball", "Cat", "Dog", "Fish", "cat", "bat", "rat"]
b = [i for i in a if i[0].isupper()]
print(b)

a = ["Apple", "Ball", "Cat", "Dog", "Fish"]
d = {i: i.lower() for i in a}
print(d)

d = {i: i * i for i in range(1, 11)}
print(d)


# Date and time
x = datetime.datetime.now()
print(x)                                                                                                                        

x = datetime.datetime.now()
for i in range(5):
    print("Hello, World!")
y = datetime.datetime.now()
print(y - x)

x = datetime.datetime.now()
print(x.strftime("%c"))


# OS Package
# os.remove(<path>)
# os.mkdir(<dir_name>)
# os.mkdir(<dir_name>, <new_name>)
# os.listdir()
"""
