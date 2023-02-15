class T_student_record:
    def __init__(self, name="", address="", class_name=""):
        self.name = name
        self.address = address
        self.class_name = class_name

my_student_1 = T_student_record("Hamza", "Akaria Compound", "12BR2")
my_student_2 = T_student_record("Abbas", "Manarat Al Riyadh", "9BR2")

filename = "Student.txt"

def append_record(record):
    line = (f"{record.name} | {record.address} | {record.class_name}\n")
    try:
        file = open(filename, "a")
        file.write(line)
        file.close()
    except IOError:
        print(f"{filename} failed to open!")

def delete_record():
    student_name = input("Please enter the name of the student you want to delete: ")
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file = open(filename, "w")
        for i in range(0, len(lines)):
            name = lines[i].split("|")[0].replace(" ", "")
            if name == student_name:
                lines[i] = ""
        [file.write(lines[i]) for i in range(0, len(lines))]
    except IOError:
        print(f"{filename} failed to open!")

def output_records():
    try:
        file = open(filename, "r")
        lines = file.readlines()
        for i in range(0, len(lines)):
            print(lines[i])
    except IOError:
        print(f"{filename} failed to open!")

append_record(my_student_2)
append_record(my_student_1)
delete_record()
# output_records()     