class Picture:
    # Private description: STRING
    # Private width: INTEGER
    # Private height: INTEGER
    # Private frame_colour: STRING
    def __init__(self, description, width, height, frame_colour):
        self.__description = description
        self.__width = width
        self.__height = height
        self.__frame_colour = frame_colour
    def get_description(self):
        return self.__description
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_frame_colour(self):
        return self.__frame_colour
    def set_description(self, description):
        self.__description = description

picture_array = []

def read_data(picture_array):
    filename = "Pictures.txt"
    try:
        file = open(filename, "r")
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            description = lines[i].replace("\n", "").strip()
            width = int(lines[i + 1].replace("\n", "").strip())
            height = int(lines[i + 2].replace("\n", "").strip())
            frame_colour = lines[i + 3].replace("\n", "").strip()
            new_picture = Picture(description, width, height, frame_colour)
            picture_array.append(new_picture)
    except IOError:
        print(f"{filename} not found!")
    return len(picture_array)

def search_pictures(frame_colour, max_width, max_height):
    appropriate_pictures = []
    frame_colour = frame_colour.strip().lower()
    for i in range(0, len(picture_array)):
        picture = picture_array[i]
        if (picture.get_frame_colour() == frame_colour) and (picture.get_width() <= max_width) and (picture.get_height() <= max_height):
            appropriate_pictures.append(picture)
    return appropriate_pictures

def main():
    num_of_pictures = read_data(picture_array)
    appropriate_pictures = search_pictures("BLACK", 100, 100)
    if len(appropriate_pictures):
        for i in range(0, len(appropriate_pictures)):
            picture = appropriate_pictures[i]
            print(picture.get_frame_colour(), picture.get_width(), picture.get_height())
    else:
        print("No pictures that match the specified requirements!")

main()