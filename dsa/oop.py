# class employee:
#     def __init__(self, name, staff_number):
#         self.__name = name
#         self.__staff_number = staff_number
#         self.__full_time_staff = True
#     def show_details(self):
#         print(f"Employee Name: {self.__name}")
#         print(f"Employee Number: {self.__staff_number}")

# class part_time(employee):
#     def __init__(self, name, staff_number):
#         employee.__init__(self, name, staff_number)
#         self.__full_time_staff = False
#         self.__hours_worked = 0
#     def get_hours_worked(self):
#         return self.__hours_worked

# class full_time(employee):
#     def __init__(self, name, staff_number):
#         employee.__init__(self, name, staff_number)
#         self.__full_time_staff = True
#         self.__yearly_salary = 0
#     def get_yearly_salary(self):
#         return self.__yearly_salary

# permanent_staff = full_time("Eric Jones", 72)
# permanent_staff.show_details()
# temporary_staff = part_time("Alice Hue", 1017)
# temporary_staff.show_details()

class shape:
    def __init__(self):
        self.__area = 0
        self.__perimeter = 0
    def area(self):
        print(f"Area: {self.__area}")
    def perimeter(self):
        print(f"Perimeter: {self.__perimeter}")

class rectangle(shape):
    def __init__(self, length, width):
        shape.__init__(self)
        self.__length = length
        self.__width = width
    def area(self):
        print(f"Area: {self.__length * self.__perimeter}")

