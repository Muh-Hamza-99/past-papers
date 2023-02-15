player_names = ["" for i in range(0, 11)]
player_scores = [0 for i in range(0, 11)]

def read_highscores():
    filename = "HighScore.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        counter = 0
        for i in range(0, len(lines), 2):
            name = lines[i].replace("\n", "").strip()
            score = int(lines[i + 1].replace("\n", "").strip())
            player_names[counter] = name
            player_scores[counter] = score
            counter += 1
        file.close()
    except IOError:
        print(f"{filename} is not found!")

def output_highscores():
    for i in range(0, len(player_names)):
        if player_names[i] != "" and player_scores != 0:
            print(f"{player_names[i]} {player_scores[i]}")

def insert_player(player_name, player_score):
    player_names[-1] = player_name
    player_scores[-1] = player_score
    length_of_arrays = len(player_names)
    for i in range(length_of_arrays - 1):
        for j in range(length_of_arrays - i - 1):
            if player_scores[j + 1] > player_scores[j]:
                player_names[j], player_names[j + 1] = player_names[j + 1], player_names[j]
                player_scores[j], player_scores[j + 1] = player_scores[j + 1], player_scores[j]

def write_top_ten():
    filename = "NewHighScore.txt"
    file = open(filename, "w")
    for i in range(0, 10):
        file.write(player_names[i])
        file.write("\n")
        file.write(str(player_scores[i]))
        file.write("\n")
    file.close()

def main():
    read_highscores()
    output_highscores()
    input_player_name = input("Please enter the player name: ")
    while len(input_player_name) != 3:
        input_player_name = input("Please enter a VALID player name: ")
    input_player_score = int(input("Please enter the player score: "))
    while input_player_score > 100000 or input_player_score < 1:
        input_player_score = int(input("Please enter a VALID player score: "))
    insert_player(input_player_name.upper(), input_player_score)
    output_highscores()
    write_top_ten()

main()