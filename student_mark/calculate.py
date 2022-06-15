def get_total(marksList):
    total = 0
    for i in marksList:
        total += i
    return total


def get_percent(marksList):
    total_scored_marks = get_total(marksList)
    total_marks = len(marksList) * 100
    percentage = (total_scored_marks / total_marks) * 100
    return percentage


def get_grade(per):
    grade = ""
    if per >= 95 and per <= 100:
        grade = "A+"
    elif per >= 90 and per <= 94.9:
        grade = "A"
    elif per >= 85 and per <= 89.9:
        grade = "B+"
    elif per >= 80 and per <= 84.9:
        grade = "B"
    elif per >= 75 and per <= 79.9:
        grade = "C+"
    elif per >= 70 and per <= 74.9:
        grade = "C"
    elif per >= 65 and per <= 69.9:
        grade = "D+"
    elif per >= 60 and per <= 64.9:
        grade = "D"
    elif per >= 00 and per <= 59.9:
        grade = "F"
    return grade
