import mysql.connector

database = mysql.connector.connect(
    host="localhost", user="root", password="", database="pythonclass4pm"
)
db = database.cursor()


"""
db.execute("SELECT * FROM students")
result = db.fetchall()
for x in result:
    print(x)
"""

# Inserting data
sql = "INSERT INTO students(name, physics, chemistry, english, nepali, total, per, grade) VALUES('Shyam', 79, 45, 54, 52, 84, 43, 'A')"
# update
sql = "UPDATE students SET name = 'Sita' WHERE sn = 19"
# delete
sql = "DELETE FROM students WHERE sn = 2"


db.execute(sql)
database.commit()
