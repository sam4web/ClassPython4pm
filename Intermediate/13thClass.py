"""
# File Handeling

# Syntax
# a = open('<file_name>', '<modes>')
# a.close()

# Modes
# r -> read
# x -> create
# w -> write
# a -> append

# x mode 
# Creates new file 
# If file exists it throws an arrows
file = open("./File/data.txt", "x")
file.close()

file = open("./File/data.txt", "r")
data = file.read()
print(data)
file.close()


# r mode
# Reads content in existing file and return it as a string
with open("./File/data.txt", "r") as file:
    data = file.read()
    str = str()
    # print(type(data))   # returns string
    print(data.split("\n"))


# w mode
# Creates new file and write content in it
# If file is already there, delets content in it and overrides
with open("./File/data.txt", "a") as file:
    file.write("Hello, World")


# a mode
# Add content in existing file
# If file doesn't exists it creates a new one
with open("./File/datda.txt", "a") as file:
    file.write("Hello, World")

# Table of 2
with open("./File/tableOfTwo.txt", "a") as file:
    for i in range(1, 11):
        file.write(f"{2} * {i} = {i * 2}\n")


bill = str()
n = int(input("Enter n: "))
for i in range(n):
    name = input("\nEnter name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
    info = f"{name},{price},{quantity},{total}\n"
    bill = bill + info

with open("./File/bill.csv", "w") as file:
    file.write("Product,Price,Quantity,Total\n")
    file.write(bill)


import os
# os.remove("../File/tableOfTwo.txt")
# print(os.listdir())
"""
