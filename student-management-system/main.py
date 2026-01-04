from manager import StudentManager
from storage import save_students, load_students


def main():
    manager = StudentManager()
    manager.students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Sort Students by Average Marks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            marks = list(map(int, input("Enter marks (space separated): ").split()))

            manager.add_student(student_id, name, age, marks)
            save_students(manager.students)
            print("Student added successfully.")

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            student_id = int(input("Enter student ID to search: "))
            student = manager.search_student(student_id)

            if student:
                student.display_details()
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            manager.delete_student(student_id)
            save_students(manager.students)

        elif choice == "5":
            manager.sort_students_by_average()
            print("Students sorted by average marks.")

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
