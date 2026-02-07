import csv
import os

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_list(self):
        return [self.student_id, self.name, self.grade]


class StudentManager:
    FILE_NAME = "students.csv"

    def __init__(self):
        self.students = {}
        self.load_students()

    def load_students(self):
        if not os.path.exists(self.FILE_NAME):
            return
        with open(self.FILE_NAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], row[1], row[2])
                self.students[row[0]] = student

    def save_students(self):
        with open(self.FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students.values():
                writer.writerow(student.to_list())

    def add_student(self, student_id, name, grade):
        if student_id in self.students:
            print("Student ID already exists!")
            return
        self.students[student_id] = Student(student_id, name, grade)
        self.save_students()
        print("Student added successfully")

    def update_student(self, student_id, name, grade):
        if student_id not in self.students:
            print("Student not found!")
            return
        self.students[student_id].name = name
        self.students[student_id].grade = grade
        self.save_students()
        print("Student updated successfully")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found!")
            return
        del self.students[student_id]
        self.save_students()
        print("Student deleted successfully")

    def list_students(self):
        if not self.students:
            print("No student records found")
            return
        print("\nStudent Records")
        print("-" * 40)
        print(f"{'ID':<10}{'Name':<20}{'Grade'}")
        print("-" * 40)
        for s in self.students.values():
            print(f"{s.student_id:<10}{s.name:<20}{s.grade}")
        print("-" * 40)

def main():
    manager = StudentManager()

    while True:
        print("""Student Management System
        1. Add Student
        2. Update Student
        3. Delete Student
        4. List Students
        5. Exit
        """)

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            manager.add_student(sid, name, grade)

        elif choice == "2":
            sid = input("Enter Student ID to update: ")
            name = input("Enter New Name: ")
            grade = input("Enter New Grade: ")
            manager.update_student(sid, name, grade)

        elif choice == "3":
            sid = input("Enter Student ID to delete: ")
            manager.delete_student(sid)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("Exiting program")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()
