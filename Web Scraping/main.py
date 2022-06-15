import plotly.graph_objects as go
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = BeautifulSoup("https://www.worldometers.info/coronavirus/", "html.parser")
soup = requests.get(url)

soup = soup.text
soup = BeautifulSoup(soup, "lxml")
soup = soup.table

tags = soup.find_all("tr")

data = []
for i in tags:
    data.append(i.text.split("\n")[1:-1])

output_data = [i for i in data if i[0] != ""]

file = open("covid.csv", "w")
x = csv.writer(file)
for i in output_data:
    x.writerow(i)

df = pd.read_csv("covid.csv", encoding="ISO-8859-1")

countries = list(df["Country,Other"][0:10])
death_data = list(df["TotalDeaths"][0:10])
final_death_data = []
for i in death_data:
    x = int(i.replace(",", ""))
    final_death_data.append(x)


fig = go.Figure([go.Bar(x=countries, y=final_death_data)])
fig.show()

import plotly.graph_objects as go

fig = go.Figure(data=[go.Pie(labels=countries, values=final_death_data)])
fig.show()
