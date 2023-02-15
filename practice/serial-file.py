FILENAME = "Serial.txt"

def read():
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    for i in range(0, len(lines)):
        student_name = lines[i].split("|")[0]
        student_major = lines[i].split("|")[1].replace("\n", "")
        print(f"{i+1} : {student_name}-{student_major}")

def write():
    student_name = input("Student Name: ")
    student_major = input("Student Major: ")
    record = f"{student_name}|{student_major}\n"
    with open(FILENAME, "a") as file:
        file.write(record)

def delete():
    position = int(input("Record you want to delete: "))
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    del lines[position - 1]
    with open(FILENAME, "w") as file:
        for i in range(0, len(lines)):
            file.write(f"{lines[i]}")            

def main():
    user_option = input("Enter letter for reading (r), deletion (d) or writing (w): ")
    while user_option != "r" and user_option != "d" and user_option != "w":
        user_option = input("Enter a valid letter for reading (r), deletion (d) or writing (w): ")
    if user_option == "r":
        read()
    elif user_option == "d":
        delete()
    elif user_option == "w":
        write()

main()