class Pictures:   #Q2, Part A 
    #Private picturedescription : STRING
    #Private framecolour : STRING
    #Private height : INTEGER
    #Private width : INTEGER
    def __init__(self,picturedescription,width,height,framecolour):
        self.__picturedescription = picturedescription
        self.__framecolour = framecolour
        self.__height = height
        self.__width = width
    def GetDescription(self):   #Q2, Part B 
        return self.__picturedescription
    def GetFrameColour(self):
        return self.__framecolour
    def GetHeight(self):
        return self.__height
    def GetWidth(self):
        return self.__width
    def SetDescription(self,Description):   #Q2, Part C
        self.__picturedescription = Description

PicturesList = []   #Q2, Part D

def ReadData(PicturesList):   #Q2, Part E
    filename = "Pictures.txt"
    try:
        file = open(filename,"r")
        # Textln = (file.readline()).strip()
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            picturedescription = lines[i].strip()
            width = int(lines[i + 1].strip())
            height = int(lines[i + 2].strip())
            framecolour = lines[i + 3].strip()
            new_picture = Pictures(picturedescription,width,height,framecolour)
            PicturesList.append(new_picture)
        file.close()
    except IOError: 
        print("The file cant be found")
    return len(PicturesList), PicturesList
NumberPicturesInArray, PicturesArray = ReadData(PicturesList)

FrameColour = input("Input the Frame colour ").lower()
MaxWidth = int(input("Input the Maximum Width "))
MaxHeight = int(input("Input the Maximum Height "))

for i in range(0, NumberPicturesInArray):
    if (PicturesArray[i].GetFrameColour() == FrameColour) and (PicturesArray[i].GetWidth() <= MaxWidth) and (PicturesArray[i].GetHeight() <= MaxHeight):
        print(PicturesArray[i].GetDescription(), " " , str(PicturesArray[i].GetWidth()), " ", str(PicturesArray[i].GetHeight())) 