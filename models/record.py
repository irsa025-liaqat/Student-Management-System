class Record:
    def __init__(self, student_id, subject_code):
        self.student_id = student_id
        self.subject_code = subject_code
        self.grades = []
        self.attendance_present = 0
        self.attendance_total = 0

    def add_grade(self, grade):
        self.grades.append(grade)

    def mark_attendance(self, present=True):
        if present:
            self.attendance_present += 1
        self.attendance_total += 1

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_attendance_percentage(self):
        if self.attendance_total == 0:
            return 0
        return (self.attendance_present / self.attendance_total) * 100

    def __str__(self):
        grades_str = ",".join(map(str, self.grades)) if self.grades else "None"
        return (f"{self.student_id} | {self.subject_code} | "
                f"grades=[{grades_str}] | attendance={self.attendance_present}/{self.attendance_total}")