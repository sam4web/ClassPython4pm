import pandas as pd

"""
df = pd.read_csv("./Data/data.csv")
print(df)
print(df.head(2))  # reads data from start
print(df.tail(2))  # reads data  from end

df = pd.read_csv("./Data/data.csv", index_col="Sn")  # Value in index_col comes first
print(df.loc[2:5])  # prints value from index 2 to 5

df = pd.read_csv("./Data/data.csv", index_col="Name")
print(df.loc["Shyam":"Nirman"])  # prints value from name 'Shyam to 'Nirman'

df = pd.read_csv("./Data/data.csv", index_col="Sn")
print(df["Address"])
print(df["Address"] == "Kathmandu")
print(df[df["Address"] == "Kathmandu"])

data = df[df["Address"] == "Kathmandu"]
data.to_csv("./Data/NewData.csv")

d = {
    "Name": ["Ram", "Shyam"],
    "Age": [23, 54],
    "Address": ["Kathmandu", "Lalitpur"],
}
data = pd.DataFrame(d)
print(data)

df = pd.read_csv("./Data/data.csv", index_col="Sn", usecols=["Sn", "Name", "Phone"])
df.to_csv("./Data/Info.csv")
print(df)

df = pd.read_csv("./Data/data.csv", index_col="Sn")
data = df[(df["Address"] == "Kathmandu") & (df["Age"] > 30)]
print(data)
"""
