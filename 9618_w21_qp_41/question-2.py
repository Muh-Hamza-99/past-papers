class Picture:
    def __init__(self, description, width, height, frame_colour):
        self.__description = description
        self.__width = width
        self.__height = height
        self.__frame_colour = frame_colour
    def set_description(self, description):
        self.__description = description
    def get_description(self):
        return self.__description
    def get_frame_colour(self):
        return self.__frame_colour
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

picture_array = []

def read_data():
    filename = "Pictures.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        for i in range(0, int(len(lines) - 1/4), 4):
            description = lines[i].replace("\n", "")
            width = int(lines[i + 1].replace("\n", ""))
            height = int(lines[i + 2].replace("\n", ""))
            frame_colour = lines[i + 3].replace("\n", "")
            new_picture = Picture(description, width, height, frame_colour)
            picture_array.append(new_picture)
        return len(picture_array)
    except IOError:
        print(f"{filename} can't be read!")

def user_requirements(frame_colour, max_width, max_height):
    appropriate_pictures = []
    frame_colour = frame_colour.strip().lower()
    for i in range(0, len(picture_array)):
        picture = picture_array[i]
        if (picture.get_frame_colour() == frame_colour) and (picture.get_width() <= max_width) and ( picture.get_height() <= max_height):
            appropriate_pictures.append(picture)
    return appropriate_pictures


def main():
    num_of_pictures = read_data()
    appropriate_pictures = user_requirements("silver", 25, 25)
    for i in range(0, len(appropriate_pictures)):
        picture = appropriate_pictures[i]
        print(picture.get_description(), picture.get_width(), picture.get_height(), picture.get_frame_colour())

main()