import mysql.connector
import pandas as pd
import os

database = mysql.connector.connect(
    host="localhost", user="root", password="", database="students_marks"
)
db = database.cursor()


def add_data(data_list):
    # Inserting data
    sql = f"INSERT INTO marks(sn, name, physics, chemistry, english, nepali, total, per, grade) VALUES({data_list[0]}, '{data_list[1]}', {data_list[2]}, {data_list[3]}, {data_list[4]}, {data_list[5]}, {data_list[6]}, {data_list[7]}, '{data_list[8]}')"
    db.execute(sql)
    database.commit()


def del_data():
    sql = "DELETE FROM marks"
    db.execute(sql)
    database.commit()


def store_data():
    # deletes old data to store new one
    try:
        os.remove("./student_mark/marks.csv")
    except:
        pass
    data = {
        "Sn": [],
        "Name": [],
        "Physics": [],
        "Chemistry": [],
        "English": [],
        "Nepali": [],
        "Total": [],
        "Percentage": [],
        "Grade": [],
    }
    # fetch all items from database
    db.execute("SELECT * FROM marks")
    result = db.fetchall()
    # items from database in dictionary
    for item in result:
        data["Sn"].append(item[0])
        data["Name"].append(item[1])
        data["Physics"].append(item[2])
        data["Chemistry"].append(item[3])
        data["English"].append(item[4])
        data["Nepali"].append(item[5])
        data["Total"].append(item[6])
        data["Percentage"].append(item[7])
        data["Grade"].append(item[8])
    # dict to csv
    df = pd.DataFrame(data)
    df.to_csv("./student_mark/marks.csv", index=False)
