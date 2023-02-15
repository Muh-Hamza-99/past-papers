# Part (a)
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    def get_question(self):
        return self.__question
    def check_answer(self, answer):
        is_correct = True if self.__answer == answer else False
        return is_correct
    def get_points(self, num_of_attempts):
        if num_of_attempts == 1:
            return self.__points
        elif num_of_attempts == 2:
            return self.__points // 2
        elif num_of_attempts == 4 or num_of_attempts == 3:
            return self.__points // 4
        else: 
            return 0

# Part (b)
array_treasure = []
def read_data():
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        for i in range(0, 15, 3):
            question = lines[i].replace("\n", "")
            answer = int(lines[i + 1].replace("\n", ""))
            points = int(lines[i + 2].replace("\n", ""))
            treasure = TreasureChest(question, answer, points)
            array_treasure.append(treasure)
    except IOError:
        print(f"Error reading {filename}!")
    

def main():
    read_data()
    question_number = int(input("Enter a question to answer: "))
    while question_number < 1 or question_number > 5:
        question_number = int(input("Enter a valid question to answer (1-5): "))
    print(array_treasure[question_number - 1].get_question())
    answer = int(input("Enter the answer: "))
    num_of_attempts = 1
    while not (array_treasure[question_number - 1].check_answer(answer)):
        answer = int(input("Oops, that isn't quite correct! Try again: "))
        num_of_attempts += 1
    points = array_treasure[question_number - 1].get_points(num_of_attempts)
    print(f"Correct! You have been awarded {points} points!")
main()