class Course:
    def __init__(self, title, max_students): # sets up a new course
        self.course_title = title
        self.max_students = max_students
        self.num_of_lessons = 0
        self.course_lesson = []
        self.course_assessment = Assessment
    def add_lesson(self, lesson_title, duration, requires_lab):
        self.num_of_lessons = self.num_of_lessons + 1
        if len(self.course_lesson) >= 50:
            print("Lessons per course full!")
        else:
            self.course_lesson.append(Lesson(lesson_title, duration, requires_lab))
    def add_assessment(self, title, max_marks):
        self.course_assessment = Assessment(title, max_marks)
    def output_course_details(self):
        print(self.course_title, "Maximum number: ", self.max_students)
        for i in range(self.num_of_lessons):
            print(self.course_lesson[i].output_lesson_details())
        # print(f"Course Assessment: {self.course_assessment.output_assessment_details()}")

class Lesson:
    def __init__(self, lesson_title, duration, requires_lab):
        self.lesson_title = lesson_title
        self.duration = duration
        self.requires_lab = requires_lab
    def output_lesson_details(self):
        print(f"{self.lesson_title} | {self.duration} | {self.requires_lab}")

class Assessment:
    def __init__(self, title, max_marks):
        self.title = title
        self.max_marks = max_marks
    def output_assessment_details(self):
        print(f"{self.title} | {self.max_marks}")

computer_science = Course("Computer Science", 100)
computer_science.add_assessment("Final Exam", 200)
computer_science.add_lesson("CS100", 120, False)
print(computer_science.output_course_details())