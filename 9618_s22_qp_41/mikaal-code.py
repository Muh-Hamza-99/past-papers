score_data = [[0 for x in range(2)] for y in range(11)]

def read_highscores():
    filename = "HighScore.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        counter = 0
        for i in range(0, len(lines), 2):
            name = lines[i].strip().replace("\n", "")
            score = int(lines[i + 1].strip().replace("\n", ""))
            score_data[counter][0] = name
            score_data[counter][1] = score
            print(counter)
            counter += 1
        file.close()
    except IOError:
        print(f"{filename} not found!")

print(score_data)
read_highscores()
print(score_data)