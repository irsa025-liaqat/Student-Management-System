class Subject:
    def __init__(self, subject_code, subject_name, credit_hours):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"{self.subject_code} | {self.subject_name} | {self.credit_hours}"