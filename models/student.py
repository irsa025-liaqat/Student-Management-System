class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section
        self.num_subjects_enrolled = 0

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.section}"