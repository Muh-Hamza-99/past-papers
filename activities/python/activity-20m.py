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

def read_record(student_id):
    try:
        file = open("Student.DAT", "rb")
        student_record = pickle.load(file)
        while student_id != student_record.student_id:
            student_record = pickle.load(file)
        print(student_record.student_name, student_record.student_class, student_record.student_id)
        file.close()
    except IOError:
        print("Something went wrong in the file!")

def main():
    user_input = input("Please enter R for reading a record or W for writing to a file: ")
    while user_input.upper() != "R" and user_input.upper() != "W":
        user_input = input("Please enter R for reading a record or W for writing to a file: ")
        print(user_input)
    if user_input == "W":
        input_record()
    else:
        student_id = int(input("Please enter the student ID: "))
        read_record(student_id)

main()