import pickle

class Student:
    def __init__(self, student_name, student_class, student_id):
        self.student_name = student_name
        self.student_class = student_class
        self.student_id = student_id

def input_record():
    student_name = input("Please enter the student: ")
    student_class = input("Please enter the student class: ")
    student_id = int(input("Please enter the student ID: "))
    new_student = Student(student_name, student_class, student_id)
    try:
        file = open("Student.DAT", "ab")
        pickle.dump(new_student, file)
        file.close()
    except IOError:
        print("Something went wrong in the file!")
    return new_student

def read_record(record):
    try:
        file = open("Student.DAT", "rb")
        student_record = pickle.load(file)
        while record.student_name != student_record.student_name:
            student_record = pickle.load(file)
        print(student_record.student_name, student_record.student_class, student_record.student_id)
        file.close()
    except IOError:
        print("Something went wrong in the file!")

def main():
    record = input_record()
    read_record(record)

main()