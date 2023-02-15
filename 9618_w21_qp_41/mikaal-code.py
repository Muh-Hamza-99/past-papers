arraynodes = [[0 for X in range(3)] for Y in range(20)]
rootpointer = -1
freenode = 0

def addnode(arraynodes,rootpointer,freenode):
    newdata = int(input("please enter the data you would like to add: "))
    if freenode <= 19:
        arraynodes[freenode][0] = -1
        arraynodes[freenode][1] = newdata
        arraynodes[freenode][2] = -1
        print(rootpointer)
        if rootpointer == -1:
            rootpointer = 0
        else:
            placed = False
            currentnode = rootpointer
            while placed == False:
                print(currentnode)
                if newdata < arraynodes[currentnode][1]:
                    if arraynodes[currentnode][0] == -1:
                        arraynodes[currentnode][0] = freenode
                        placed = True
                    else:
                        currentnode = arraynodes[currentnode][0]
                else:
                    if arraynodes[currentnode][2] == -1:
                        arraynodes[currentnode][2] = freenode
                        placed = True
                    else:
                        currentnode = arraynodes[currentnode][2]
        freenode = freenode + 1
    else:
        print("the tree is full")    
    return arraynodes, rootpointer, freenode

def printall(arraynodes):
    for i in range(0, len(arraynodes)):
        print(str(arraynodes[i][0]), str(arraynodes[i][1]), str(arraynodes[i][2]))
        
for i in range(0, 10):
    addnode(arraynodes, rootpointer, freenode)
print(arraynodes)