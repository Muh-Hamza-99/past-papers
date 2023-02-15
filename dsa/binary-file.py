import pickle
import datetime

class Student:
    def __init__(self):
        self.name = ""
        self.register_number = 0
        self.date_of_birth = datetime.datetime.now()
        self.full_time = True

student_record = Student()
student_file = open("students.DAT", "w+b")
print("Please enter student details: ")
student_record.name = input("Please enter student name: ")
student_record.register_number = int(input("Please enter student register number: "))
year = int(input("Please enter the student's year of birth: "))
month = int(input("Please enter the student's month of birth: "))
day = int(input("Please enter the student's day of birth: "))
student_record.date_of_birth = datetime.datetime(year, month, day)
student_record.full_time = bool(input("Please enter True for full-time or False for part-time: "))
pickle.dump(student_record, student_file)
student_file.close()
student_file = open("students.DAT", "rb")
student_record = pickle.load(student_file)
print(student_record.name, student_record.register_number, student_record.date_of_birth, student_record.full_time)
student_file.close()