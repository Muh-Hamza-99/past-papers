class TreasureChest:
    # Private question: STRING
    # Private answer: INTEGER
    # Private points: INTEGER
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    def get_question(self):
        return self.__question
    def check_answer(self, answer):
        return True if answer == self.__answer else False
    def get_points(self, num_of_attempts):
        if num_of_attempts == 1:
            return self.__points
        elif num_of_attempts == 2:
            return self.__points // 2
        elif num_of_attempts == 4 or num_of_attempts == 3:
            return self.__points // 4
        else: 
            return 0

array_treasure = []

def read_data():
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            question = lines[i].replace("\n", "").strip()
            answer = int(lines[i + 1].replace("\n", "").strip())
            points = int(lines[i + 2].replace("\n", "").strip())
            treasure_chest = TreasureChest(question, answer, points)
            array_treasure.append(treasure_chest)
    except IOError:
        print(f"{filename} not found!")

def main():
    read_data()
    question_number = int(input("Please enter a question number: "))
    while question_number < 1 or question_number > 5:
        question_number = int(input("Please enter a VALID question number: "))
    print(array_treasure[question_number - 1].get_question())
    user_answer = int(input("Please enter the answer: "))
    num_of_attempts = 1
    while not (array_treasure[question_number - 1].check_answer(user_answer)):
        num_of_attempts += 1
        user_answer = int(input("Wrong! Please enter the CORRECT answer: "))
    user_points = array_treasure[question_number - 1].get_points(num_of_attempts)
    print(user_points)

main()