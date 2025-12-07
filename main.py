from models.manager import SystemManager

def main():
    manager = SystemManager()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Enroll Student")
        print("4. Add Grade")
        print("5. Mark Attendance")
        print("6. View Student Report")
        print("7. View All Students")
        print("8. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            section = input("Enter Section/Batch: ")
            if manager.add_student(sid, name, section):
                print("Student added successfully.")
            else:
                print("Error: Student ID already exists.")

        elif choice == "2":
            code = input("Enter Subject Code: ")
            name = input("Enter Subject Name: ")
            credits = int(input("Enter Credit Hours: "))
            if manager.add_subject(code, name, credits):
                print("Subject added successfully.")
            else:
                print("Error: Subject Code already exists.")

        elif choice == "3":
            sid = input("Enter Student ID: ")
            code = input("Enter Subject Code: ")
            if manager.enroll_student(sid, code):
                print("Student enrolled successfully.")
            else:
                print("Error: Invalid Student ID or Subject Code, or already enrolled.")

        elif choice == "4":
            sid = input("Enter Student ID: ")
            code = input("Enter Subject Code: ")
            grade = int(input("Enter Grade: "))
            if manager.add_grade(sid, code, grade):
                print("Grade added successfully.")
            else:
                print("Error: Enrollment not found.")

        elif choice == "5":
            sid = input("Enter Student ID: ")
            code = input("Enter Subject Code: ")
            present = input("Present? (y/n): ").lower() == 'y'
            if manager.mark_attendance(sid, code, present):
                print("Attendance marked.")
            else:
                print("Error: Enrollment not found.")

        elif choice == "6":
            sid = input("Enter Student ID: ")
            report = manager.view_student_report(sid)
            if report:
                print(report)
            else:
                print("Student not found.")

        elif choice == "7":
            print(manager.view_all_students())

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
