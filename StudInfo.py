class StudInfo:
    def __init__(self, f_name, age, quiz_grade):
        self.f_name = f_name
        self.age = age
        self.quiz_grade = quiz_grade
        self.status = None  

    def student_grading(self):
        if self.quiz_grade == "none":
            self.status = None  # Student has not taken the quiz
        elif self.quiz_grade>= passing_grade:
            self.status = True  # Passed
        else:
            self.status = False  # Failed

    def display_info(self):
        print(f"Student Name: {self.f_name}")
        print(f"Age: {self.age}")
        print(f"Quiz Score: {self.quiz_grade}")
        print(f"Passed: {self.status}")

# The constant set as the variable for the passing grade
passing_grade = 7.5

f_name = "Matteo"
age = 21
quiz_grade = "none"

#quiz not submitted
student = StudInfo(f_name, age, quiz_grade)
student.student_grading()

print("\nStudent has not submitted quiz:")
student.display_info()

# int variable passing grade
quiz_grade = 8 
student.quiz_grade = quiz_grade
student.student_grading()

print("\nPassed Quiz Score:")
student.display_info()

# float variable failed
quiz_grade = 7.2  # Changing from int to float
student.quiz_grade = quiz_grade
student.student_grading()

print("\nFailed Quiz Score:")
student.display_info()
