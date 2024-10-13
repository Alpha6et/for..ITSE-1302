#Lesson 6 Assignment
grade_book = {}
def names():
    print("\nStudent Names: \n")
    for id, details in grade_book.items():
        print(details["Name"])
    print()       
def details():
    print("\nAccessing student information.\n")       
    print("Name\tID\tGPA\tHours\tGrades")
    for id, details in grade_book.items():
        name = details["Name"]
        gpa = details["GPA"]
        hours = details["Hours"]
        grades = ",".join(map(str, details["Grades"]))
        print(f"{name}\t{id}\t{gpa}\t{hours}\t{grades}")
def remove(grade_book, id):
    if id in grade_book:
        name=grade_book[id]["Name"]
        grade_book.pop(id)
        print(f"\n{name} has dropped the class and is being removed from grade book.\n")
        print(grade_book)
        return name
    else:
        print("Student not found.")
def get_gpa(grade_book,id):
    if id in grade_book:
        name=grade_book[id]["Name"]
        gpa=grade_book[id]["GPA"]
        grade_book.get(gpa)
        print(f"\n{name}'s GPA is {gpa}.\n")
    else:
        print("Student not found.")
def clear_grades(grade_book):
    print("\nStudents have graduated. Clearing grade book.\n")
    grade_book.clear()
    print(grade_book)
def main():
    grade_book['1'] = {
    "Name":"Anna",
    "ID" :"1",
    "GPA":"2.9",
    "Hours":"6",
    "Grades": [85,79,72,89]
    }
    grade_book['2'] = {
    "Name":"Ben",
    "ID":"2",
    "GPA" : "3.0",
    "Hours":"60",
    "Grades": [90,82,86,93]
    }
    grade_book['3'] = {
    "Name":"Cassie",
    "ID":"3",
    "GPA":"2.5",
    "Hours":"24",
    "Grades": [90,88,71,80]
    }
    grade_book['4'] = {
    "Name":"Daniel",
    "ID":"4",
    "GPA":"3.5",
    "Hours":"12",
    "Grades" : [89,95,90,92]
    }
    print(grade_book)
    names()
    details()
    remove(grade_book, '3')
    get_gpa(grade_book, '1')
    clear_grades(grade_book)
main()
print("Completed by Laura Bartlett")
