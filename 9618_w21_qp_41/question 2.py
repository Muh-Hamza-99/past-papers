


class Picture:
    #PRIVATE Pdescription : STRING
    #PRIVATE Pwidth : INTEGER
    #PRIVATE Pheight : INTEGER
    #PRIVATE Pframecolour : STRING
    def __init__(self, Pdescription, Pwidth, Pheight, Pframecolour):
        self.__Description = Pdescription
        self.__Width = Pwidth
        self.__Height = Pheight 
        self.__FrameColour = Pframecolour

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetFrameColour(self):
        return self.__FrameColour

    def SetDescription(self,newdescription):
        self.__Description = newdescription


myArray = [Picture for i in range(21)]


def ReadData():
    global myArray
    try:    
        filename = ("Pictures.txt")
        file = open(filename,"r")
        lines = file.readlines()
        filelength = len(lines)
        counter = 0
        for i in range(0,filelength,4):
            descrption = lines[i].replace("\n","")
            width = int(lines[i+1].replace("\n",""))
            height = int(lines[i+2].replace("\n",""))
            framecolour = lines[i+3].replace("\n","")
            item = Picture(descrption,width,height,framecolour)
            myArray[counter] = item
            counter += 1
        file.close()
        return len(myArray)
    except IOError:
        print("file not found")


result = ReadData()
print(result)


framecolour = input("Please enter the frame colour you are looking for: ").lower()
maxwidth = int(input("Please enter the maximum width you would like: "))
maxheight = int(input("Please enter the maximum height you would like: "))


for counter in range(len(myArray)):
    tempframcolour = myArray[counter].GetFrameColour()
    tempwidth = myArray[counter].GetWidth()
    tempheight = myArray[counter].GetHeight()
    tempdescription = myArray[counter].GetDescription()
    if tempframcolour == framecolour and maxwidth <= tempwidth and maxheight <= tempheight:
        print(f"picture desription: {tempdescription} | width: {tempwidth} | height: {tempheight}")

    #ms ans (still doesnt work)
    # if myArray[counter].GetFrameColour() == framecolour and maxwidth >= myArray[counter].GetWidth() and maxheight >= myArray[counter].GetHeight():
    #     print(f"picture desription: {myArray[counter].GetFrameColour()} | width: {myArray[counter].GetWidth()} | height: {myArray[counter].GetHeight()}")
        


