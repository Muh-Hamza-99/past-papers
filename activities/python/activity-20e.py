import math

class shape:
    def __init__(self):
        self.__area = 0
        self.__perimeter = 0
    def area(self):
        print(f"Area: {self.__area}")
    def perimeter(self):
        print(f"Perimeter: {self.__perimeter}")

class Rectangle(shape):
    def __init__(self, length, width):
        shape.__init__(self)
        self.__length = length
        self.__width = width
    def area(self):
        print(f"Area: {self.__length * self.__width}")
    def perimeter(self):
        print(f"Perimeter: {2 * (self.__length + self.__width)}")

class Triangle(shape):
    def __init__(self, base, height):
        shape.__init__(self)
        self.__base = base
        self.__height = height
    def area(self):
        print(f"Area: {self.__base * self.__height * 0.5}")

class Circle(shape):
    def __init__(self, radius):
        shape.__init__(self)
        self.__radius = radius
    def area(self):
        print(f"Area: {math.pi * (self.__radius) ** 2}")
    def perimeter(self):
        print(f"Perimeter: {2 * self.__radius * math.pi}")

circle = Circle(5)
circle.area()