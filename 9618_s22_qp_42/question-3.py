class Card:
    # PRIVATE colour : STRING
    # PRIVATE number : INTEGER
    def __init__(self, number, colour):
        self.__number = number
        self.__colour = colour
    def get_colour(self):
        return self.__colour
    def get_number(self):
        return self.__number

cards = [Card for i in range(30)]
selected_cards = []

def choose_card():
    user_card_input = int(input("Please enter a card number: "))
    while user_card_input > 30 or user_card_input < 1:
        user_card_input = int(input("Please enter a card number between 1 and 30: "))
    if (user_card_input - 1) in selected_cards:
        return None
    else:
        selected_cards.append(user_card_input - 1)
        return user_card_input

def main():
    filename = "CardValues.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        counter = 0
        for i in range(0, len(lines), 2):
            number = int(lines[i].strip().replace("\n", ""))
            colour = lines[i + 1].strip().replace("\n", "")
            cards[counter] = Card(number, colour)
            counter += 1
    except IOError:
        print(f"{filename} is not found!")
    
    player_1 = []
    while len(player_1) != 4:
        card_index = choose_card()
        if card_index is not None:
            player_1.append(cards[card_index])
        else:
            print("Card taken!")
    for i in range(0, len(player_1)):
        print(f"Card Colour: {player_1[i].get_colour()} | Card Number: {player_1[i].get_number()}")
main()