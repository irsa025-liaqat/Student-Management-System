import os
from .student import Student
from .subject import Subject
from .record import Record

class SystemManager:
    def __init__(self):
        self.students = {}
        self.subjects = {}
        self.records = []
        self.data_dir = "data"
        self.load_all_data()

    # === FILE HANDLING ===
    def load_all_data(self):
        os.makedirs(self.data_dir, exist_ok=True)
        self.load_students()
        self.load_subjects()
        self.load_records()

    def save_students(self):
        with open(os.path.join(self.data_dir, "students.txt"), "w") as f:
            for student in self.students.values():
                f.write(f"{student}\n")

    def save_subjects(self):
        with open(os.path.join(self.data_dir, "subjects.txt"), "w") as f:
            for subject in self.subjects.values():
                f.write(f"{subject}\n")

    def save_records(self):
        with open(os.path.join(self.data_dir, "records.txt"), "w") as f:
            for record in self.records:
                f.write(f"{record}\n")

    def load_students(self):
        try:
            with open(os.path.join(self.data_dir, "students.txt"), "r") as f:
                for line in f:
                    parts = line.strip().split(" | ")
                    if len(parts) == 3:
                        student = Student(parts[0], parts[1], parts[2])
                        self.students[parts[0]] = student
        except FileNotFoundError:
            pass

    def load_subjects(self):
        try:
            with open(os.path.join(self.data_dir, "subjects.txt"), "r") as f:
                for line in f:
                    parts = line.strip().split(" | ")
                    if len(parts) == 3:
                        subject = Subject(parts[0], parts[1], int(parts[2]))
                        self.subjects[parts[0]] = subject
        except FileNotFoundError:
            pass

    def load_records(self):
        try:
            with open(os.path.join(self.data_dir, "records.txt"), "r") as f:
                for line in f:
                    parts = line.strip().split(" | ")
                    if len(parts) >= 3:
                        record = Record(parts[0], parts[1])
                        # Parse grades
                        if "grades=[" in parts[2]:
                            grades_str = parts[2].split("=[")[1].rstrip("]")
                            if grades_str and grades_str != "None":
                                record.grades = list(map(int, grades_str.split(",")))
                        # Parse attendance
                        if len(parts) > 3 and "attendance=" in parts[3]:
                            att_str = parts[3].split("=")[1]
                            present, total = map(int, att_str.split("/"))
                            record.attendance_present = present
                            record.attendance_total = total
                        self.records.append(record)
        except FileNotFoundError:
            pass

    # === CORE OPERATIONS ===
    def add_student(self, student_id, name, section):
        if student_id in self.students:
            return False
        self.students[student_id] = Student(student_id, name, section)
        self.save_students()
        return True

    def add_subject(self, subject_code, name, credit_hours):
        if subject_code in self.subjects:
            return False
        self.subjects[subject_code] = Subject(subject_code, name, credit_hours)
        self.save_subjects()
        return True

    def enroll_student(self, student_id, subject_code):
        if student_id not in self.students or subject_code not in self.subjects:
            return False
        for rec in self.records:
            if rec.student_id == student_id and rec.subject_code == subject_code:
                return False
        self.records.append(Record(student_id, subject_code))
        self.students[student_id].num_subjects_enrolled += 1
        self.save_records()
        return True

    def add_grade(self, student_id, subject_code, grade):
        for rec in self.records:
            if rec.student_id == student_id and rec.subject_code == subject_code:
                rec.add_grade(grade)
                self.save_records()
                return True
        return False

    def mark_attendance(self, student_id, subject_code, present):
        for rec in self.records:
            if rec.student_id == student_id and rec.subject_code == subject_code:
                rec.mark_attendance(present)
                self.save_records()
                return True
        return False

    # === REPORTING ===
    def view_student_report(self, student_id):
        if student_id not in self.students:
            return None
        student = self.students[student_id]
        report = f"Student ID: {student_id}\nName: {student.name}\nSection: {student.section}\n\n"
        subject_records = [r for r in self.records if r.student_id == student_id]
        if not subject_records:
            report += "No subjects enrolled.\n"
            return report
        for rec in subject_records:
            sub = self.subjects.get(rec.subject_code, None)
            sub_name = sub.subject_name if sub else "Unknown"
            report += f"Subject: {sub_name} ({rec.subject_code})\n"
            report += f"  Grades: {rec.grades if rec.grades else 'None'} | Avg: {rec.get_average_grade():.2f}\n"
            report += f"  Attendance: {rec.attendance_present}/{rec.attendance_total} ({rec.get_attendance_percentage():.2f}%)\n\n"
        return report

    def view_all_students(self):
        report = "All Students:\n"
        for sid, student in self.students.items():
            report += f"{sid}: {student.name} - {student.section} (Subjects: {student.num_subjects_enrolled})\n"
        return report