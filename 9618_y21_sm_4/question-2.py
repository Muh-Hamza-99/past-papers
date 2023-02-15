class HiddenBox:
    # PRIVATE box_name : STRING
    # PRIVATE creator : STRING
    # PRIVATE date_hidden : DATE
    # PRIVATE game_location : STRING
    # PRIVATE last_finds : ARRAY [0:9] OF STRING
    # PRIVATE active : BOOLEAN 
    def __init__(self, box_name, creator, date_hidden, game_location):
        self.__box_name = box_name
        self.__creator = creator
        self.__date_hidden = date_hidden
        self.__game_location = game_location
        self.__last_finds = []
        self.__active = False
    def get_box_name(self):
        return self.__box_name
    def get_game_location(self):
        return self.__game_location

class PuzzleBox(HiddenBox):
    def __init__(self, box_name, creator, date_hidden, game_location, puzzle_test, solution):
        HiddenBox.__init__(self, box_name, creator, date_hidden, game_location)
        self.__puzzle_text = puzzle_test
        self.__solution = solution

def new_box(the_boxes):
    box_name = input("Please enter the box name: ")
    creator = input("Please enter the creator of this box: ")
    date_hidden = input("Please enter the date this box is created: ")
    game_location = input("Please enter the location where you want to hide the box: ")
    new_hidden_box = HiddenBox(box_name, creator, date_hidden, game_location)
    the_boxes[-1] = new_hidden_box
    
def main():
    the_boxes = [HiddenBox for i in range(10000)]
    new_box(the_boxes)

main()