import random

class Island:
    def __init__(self):
        self.__grid = [["." for i in range(30)]for i in range(0, 10)]
    def get_square(self, row, column):
        return self.__grid[row][column]
    def hide_treasure(self):
        random_row, random_column = random.randint(0, 9), random.randint(0, 29)
        while self.__grid[random_row][random_column] == "T":
            random_row, random_column = random.randint(0, 9), random.randint(0, 29)
        self.__grid[random_row][random_column] = "T"
    def dig_hole(self, row, column):
        location = self.__grid[row][column]
        if location == ".":
            self.__grid[row][column] = "O"
        elif location == "T":
            self.__grid[row][column] = "X"

def display_grid(island):
    for i in range(0, 10):
        row = ""
        for j in range(0, 30):
            row += f"{island.get_square(i, j)} "
        print(row)

def start_digging(island):
    row = int(input("Please enter the row number: "))
    while row > 10 or row < 1:
        row = int(input("Please enter the row number between 1 and 30: "))
    column = int(input("Please enter the column number: "))
    while column > 30 or column < 1:
        column = int(input("Please enter the column number between 1 and 30: "))
    island.dig_hole(row, column)


def main():
    island = Island()
    display_grid(island)
    for i in range(0, 3):
        island.hide_treasure()
        display_grid(island)
    # start_digging()
    # display_grid()

main()