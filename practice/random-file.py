import pickle

FILENAME = "Random.DAT"

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

def write():
    try:
        student_id = int(input("Student ID (1-20): "))
        while student_id < 1 or student_id > 20:
            student_id = int(input("Student ID (1-20): "))
        student_name = input("Student Name: ")
        new_student = f"{student_id}-{student_name}"
        file = open(FILENAME, "rb+")
        file.seek(int(student_id * 2) - 1)
        pickle.dump(new_student, file)
    except IOError:
        print(f"{FILENAME} doesn't exist!")
    finally:
        file.close()

def read():
    try:
        student_id = int(input("Student ID (1-20): "))
        while student_id < 1 or student_id > 20:
            student_id = int(input("Student ID (1-20): "))
        file = open(FILENAME, "rb+")
        file.seek(int(student_id * 2) - 1)
        student_record = pickle.load(file)
        print(student_record)
    except IOError:
        print(f"{FILENAME} doesn't exist!")
    finally:
        file.close()

def delete():
    try:
        student_id = int(input("Student ID (1-20): "))
        while student_id < 1 or student_id > 20:
            student_id = int(input("Student ID (1-20): "))
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        del lines[student_id - 1]
        file = open(FILENAME, "rb+")
        init_file()
        for line in lines:
            pickle.dump(line, file)
    except IOError:
        print(f"{FILENAME} doesn't exist!")
    finally:
        file.close()

def init_file():
    with open(FILENAME, "w") as file:
        for i in range(19):
            file.write("\n")

def main():
    init_file()
    write()
    read()
    delete()

main()