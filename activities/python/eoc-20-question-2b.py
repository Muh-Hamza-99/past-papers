class Student:
    def __init__(self, student_name, student_dob):
        self.__student_name = student_name
        self.__student_dob = student_dob
    def show_student_name(self):
        print(self.__student_name)
    def show_student_dob(self):
        print(self.__student_dob)

class FullTimeStudent(Student):
    def __init__(self, student_name, student_dob, student_address="", student_telephone=""):
        Student.__init__(self, student_name, student_dob)
        self.__student_address = student_address
        self.__student_telephone = student_telephone
    def show_student_address(self):
        print(self.__student_address)
    def show_student_telephone(self):
        print(self.__student_telephone)

new_student = FullTimeStudent(student_name="A. Nyone", student_dob="12/11/1990", student_telephone="099111")