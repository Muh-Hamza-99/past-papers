class player:
    def __init__(self, playername, score):
        self.name = playername
        self.score = score

playerdata = [player for i in range(11)]


def ReadHighScores():
    global playerdata
    index = 0
    filename = "HighScore.txt"
    try:
        file = open(filename,"r")
        lines = file.readlines()
        lengthoffile = len(lines)
        for counter in range(0,lengthoffile,2):
            newname = lines[counter].replace("\n","")
            newscore = int(lines[counter+1].replace("\n",""))
            newitem = player(newname,newscore)
            playerdata[index] = newitem
            index = index + 1
        playerdata[10] = player(None,None)
    except IOError:
        print("File not found")


def OutputHighScore(list):
    for index in range(len(list)):
        if playerdata[index].name is not None:
            print(f"{list[index].name} | {list[index].score}")

def newtop10(newname,newscore):
    global playerdata
    playerdata[10] = player(newname,newscore)       

    for i in range(len(playerdata)):
        for j in range(len(playerdata)-1):
            if playerdata[j].score < playerdata[j+1].score :
                temp = playerdata[j]
                playerdata[j] = playerdata[j+1]
                playerdata[j+1] = temp


def WriteTopTen():
    filenam = "NewHighScore2.txt"
    try:
        file = open(filenam,"a")
        for counter in range(0,10):
            file.write(playerdata[counter].name)
            file.write("\n")
            file.write(str(playerdata[counter].score))
            file.write("\n")

    except IOError:
        print("file not found")


newname = input("Please enter a 3 letter name: ").upper()
while len(newname) != 3:
    newname = input("Please enter a valid 3 letter name: ")

newscore = int(input("Please enter a score between 1 - 100,000 (inclusive): "))
while newscore > 100000 and newscore < 1:
    newname = input("Please enter a valid 3 letter name: ")


ReadHighScores()
print("before inserting: ")
OutputHighScore(playerdata)
newtop10(newname,newscore)
print("after inserting: ")
OutputHighScore(playerdata)
WriteTopTen()

