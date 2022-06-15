import random

import mysql.connector

database = mysql.connector.connect(
    host="localhost", user="root", password="", database="pythonclass4pm"
)
db = database.cursor()


def rand_num():
    return random.randint(0, 100)


name_list = [
    "April Reiter",
    "Alice Trotter",
    "Emory Miller",
    "Mary Flanagan",
    "James Harrell",
    "David Ballin",
    "Virginia Rios",
    "Nicolas White",
    "Thomas Wheeler",
    "Velda Grubb",
]


db.execute("SELECT * FROM students")
result = db.fetchall()
n = result[len(result) - 1][0]
print(n)
for i, n in enumerate(range(len(name_list))):
    sql = f"INSERT INTO students(sn, name, physics, chemistry, english, nepali, total, per, grade) VALUES({n}, '{name_list[i]}', {rand_num()}, {rand_num()}, {rand_num()}, {rand_num()}, {rand_num()}, {rand_num()}, '{rand_num()}')"
    # sql = f"INSERT INTO students SET name = '{name_list[i]}' WHERE sn = {n}"
    db.execute(sql)
    database.commit()
