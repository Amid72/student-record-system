import json
from student import Student


FILE_NAME = "data.json"


def save_students(students):
    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "marks": student.marks
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            if file.read().strip() == "":
                return []

            file.seek(0)
            data = json.load(file)

        students = []
        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["marks"]
            )
            students.append(student)

        return students

    except FileNotFoundError:
        return []
