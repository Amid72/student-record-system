from student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, marks):
        student = Student(student_id, name, age, marks)
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display_details()
            print("-" * 20)

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def sort_students_by_average(self):
        self.students.sort(key=lambda s: s.calculate_average(), reverse=True)
