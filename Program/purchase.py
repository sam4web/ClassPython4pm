import pandas as pd

num = int(input("Enter no. of items you have purchased: "))
data = {"Sn.": list(), "Name": list(), "Quantity": list(), "Price": list()}
total = 0

for i in range(num):
    sn = i + 1
    name = input(f"\nEnter name of item #{sn}: ")
    price = int(input(f"Enter price of item #{sn}: "))
    quantity = int(input(f"Enter quantity of item #{sn}: "))
    total += price * quantity

    data["Sn."].append(sn)
    data["Name"].append(name)
    data["Price"].append(price)
    data["Quantity"].append(quantity)

print(f"Total: {total}")

df = pd.DataFrame(data)
df.to_csv("purchase.csv", index=False)

print(df)
