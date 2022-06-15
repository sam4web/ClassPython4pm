import calculate
import database_manage


def main():
    no = int(input("\nEnter no. of students: "))

    for i in range(no):
        sn = i + 1
        name = input("\nEnter student name: ")
        print("Enter marks in physics, chemistry, english & nepali seperated by Space:")
        # marks in array
        marks = input().split(" ")
        for n in range(len(marks)):
            marks[n] = int(marks[n])
        # calculation
        name = name.lower().capitalize()
        total_marks = calculate.get_total(marks)
        percentage = calculate.get_percent(marks)
        grade = calculate.get_grade(percentage)
        # data
        data = [
            sn,
            name,
            marks[0],
            marks[1],
            marks[2],
            marks[3],
            total_marks,
            percentage,
            grade,
        ]
        database_manage.add_data(data)


# main
if __name__ == "__main__":
    # delets old data
    database_manage.del_data()
    main()
    # store data in csv file
    database_manage.store_data()
