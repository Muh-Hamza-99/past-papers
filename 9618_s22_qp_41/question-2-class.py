class Balloon:
    # PRIVATE health : INTEGER
    # PRIVATE colour : STRING
    # PRIVATE defence_item : STRING
    def __init__(self, colour, defence_item):
        self.__health = 100
        self.__colour = colour
        self.__defence_item = defence_item
    def get_defence_item(self):
        return self.__defence_item
    def change_health(self, health):
        self.__health = self.__health + health
    def check_health(self):
        return True if self.__health <= 0 else False

def defend(balloon):
    opponent_strength = int(input("Please enter your opponent strength: "))
    balloon.change_health(-opponent_strength)
    print(f"Balloon defence item: {balloon.get_defence_item()}")
    health_status = balloon.check_health()
    message = "You have been defeated!" if health_status else "Keep going!"
    print(message)
    return balloon

def main():
    colour = input("Enter a colour for your balloon: ")
    defence_item = input("Enter a defence item for your balloon: ")
    balloon1 = Balloon(colour, defence_item)
    balloon1 = defend(balloon1)

main()