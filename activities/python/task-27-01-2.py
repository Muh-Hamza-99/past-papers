import datetime

class Company:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__last_contacted = str(datetime.datetime.now())
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_last_contacted(self):
        return self.__last_contacted
    def update_last_contacted(self):
        self.__last_contacted = str(datetime.datetime.now())

apple = Company("Apple", "apple.co@apple.com")
print(apple.get_email())
print(apple.get_name())
print(apple.get_last_contacted())
apple.update_last_contacted()
print(apple.get_last_contacted())