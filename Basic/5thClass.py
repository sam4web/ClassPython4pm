'''
# String 
# - Sequence of char
# - immutable datatype

a = "Hello, World!"
print(a)
print(type(a))

# Concatenation 
a = "Hello "
b = "World"
c = a + b
print(c)

# Enlargement
a = "Hello World\n"
print(a * 2)

# input() - always returns string
a = input("Enter a: ")
print(type(a))

# String slicing
a = "Hello World I am Python"
print(a[0])     # Prints first letter of String (index 0)
print(a[0:5])   # Prints from index 0 to 5 (not including 5)
print(a[5:])    # Prints from index 5
print(a[0::2])  # Prints from index 0 jumping 1 index each time
print(a[::-1])  # Reverse a string

# Strnig formating
name = "Ram"
age = 34
add = "Kathmandu"
info = "Hello World I am " + name + ". I am from " + "add" + ". I am " + str(age) + "."     # Concatenation
info = f"Hello World I am {name}. I am from {add}. I am {age}."                             # Formating
print(info)

bill = str()
n = int(input("Enter n: "))
for i in range(n):
    name = input("\nEnter name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
    info = f"{name}\t\t{price}\t\t{quantity}\t\t{total}\n"
    bill = bill + info

print(f"Name\t\tPrice\t\tQuantity\tTotal")
print(bill)

a = "Ram Shyam Hari Sita Gita Nita Nabin Ram".lower()
search = input("Enter name to search: ").lower()
if search in a:
    print("Yes")
    print(a.count(search))
else:
    print("No")

a = "Jack Lisa Dan John Danny Robert Nick Sam"
print(a.upper())                    # Changes string to lower case
print(a.title())                    # Capitalize first & each letter after space
print(a.lower())                    # Changes string to lower case
print(a.replace("Lisa ", "Rose "))  # Replace Lisa with Rose
print(a.replace("Dan ", ""))        # Removes Dan
'''
