import random

class Animal:
    def __init__(self):
        self.__across = random.randint(0, 39)
        self.__down = random.randint(0, 39)
        self.__score = 0
    def set_across(self, across):
        self.__across = across
    def get_across(self):
        return self.__across

def generate_change_in_coordinate(coordinate):
    minimum_change = -1
    maximum_change = 1
    if coordinate == 0:
        minimum_change = 0
    elif coordinate == 39:
        maximum_change = 0
    return random.randint(minimum_change, maximum_change)


class Desert:
    def __init__(self):
        self.__step_counter = 0
        self.__grid = [[" " for i in range(40)] for i in range(40)]
        self.__animal_list = [Animal for i in range(5)]
        self.__food = generate_food()