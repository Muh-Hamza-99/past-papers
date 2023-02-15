class student:
    def __init__(self, name, date_of_birth, exam_mark):
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__exam_mark = exam_mark
    def display_exam_mark(self):
        print(f"Name: {self.__name}  |  Exam mark: {self.__exam_mark}")
    
class parttime_student(student):
    def __init__(self, name, date_of_birth, exam_mark):
        student.__init__(self, name, date_of_birth, exam_mark)
        self.__fulltime_student = False

class fulltime_student(student):
    def __init__(self, name, date_of_birth, exam_mark):
        student.__init__(self, name, date_of_birth, exam_mark)
        self.__parttime_student = True

fulltime = fulltime_student("Ghuffran", "20/10/2005", 50)
fulltime.display_exam_mark()
parttime = parttime_student("Iftikhar", "9/5/1992", 100)
parttime.display_exam_mark()
