class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getquestion(self):
        return self.__question

    def checkAnswer(self, user_ans):
        if self.__answer == user_ans:
            return True
        else:
            return False

    def getPoints(self, attemptnum):
        if attemptnum == 1:
            return self.__points
        elif attemptnum == 2:
            return (self.__points // 2) # Asked for DIV operator, not normal division
        elif attemptnum == 3 or attemptnum == 4:
            return (self.__points // 4) # Asked for DIV operator, not normal division
        else:
            return 0 

arrayTreasure = [TreasureChest for i in range(5)] # Don't need to do TreasureChest(0,0,0)
def readdata():
    global arrayTreasure
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, 'r')
        # A 'while' loop makes the whole thing complicated, since in your code, you initially get a question before the loop.
        # Because of that, you read one line before the loop, and your question doesn't get updated accordingly.
        # Instead, just iterate over the file the number of times you need to using a 'for' loop; it is much simpler.
        # Changes to this are: no 'indexation' variable, just 'i' from for loop; int values
        for i in range(0, 5):
            question = file.readline().replace("\n", "")
            answer = int(file.readline().replace("\n", "")) # Better to store these as int values so that comparison and right answer can be easily calculated and checked.
            points = int(file.readline().replace("\n", "")) # Better to store these as int values so that comparison and right answer can be easily calculated and checked.
            Newitem = TreasureChest(question, answer, points)
            arrayTreasure[i] = Newitem
        file.close()
    except IOError:
        print("error")

def main():
    readdata()
    question_input = int(input("enter a num from 1 to 5: "))
    while question_input > 5 or question_input < 1:
        question_input = int(input("enter a num from 1 to 5: "))

    # In the next line, remember that the question input you get is one number greater than it's actual index in the arrayTreasure.
    # If the user enters question 3, it's index in arrayTreasure is actually 2 and not 3. This was causing an 'out of range' error for 
    # when you wanted to enter question 5.
    # Same error occurs on lines: 56, 61, 64, 71, 74
    questionOutput = arrayTreasure[question_input - 1].getquestion()
    print(questionOutput)

    answerinput = int(input("enter an answer"))

    correctanswer = arrayTreasure[question_input - 1].checkAnswer(answerinput)

    if correctanswer == True:
        points = arrayTreasure[question_input - 1].getPoints(1)
        print(points)

    else:
        attempts = 1
        while correctanswer == False:
            answerinput = int(input("try again")) # Forgot the input function
            correctanswer = arrayTreasure[question_input - 1].checkAnswer(answerinput)
            attempts = attempts + 1

        points = arrayTreasure[question_input - 1].getPoints(attempts)
        print(points)




main()