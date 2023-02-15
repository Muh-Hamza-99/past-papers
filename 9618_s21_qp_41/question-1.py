class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linked_list = [None for i in range(0, 9)]
initialisation_data = [1, 5, 6, 7, 2, 0, 0, 56, 0, 0]
initialisation_nextNode = [1, 4, 7, -1, 2, 6, 8, 3, 9, -1]
for i in range(0, 9):
    newNode = Node(initialisation_data[i], initialisation_nextNode[i])
    linked_list[i] = newNode
startPointer = 0
emptyList = 5

def outputNodes(linked_list, start_pointer):
    item_pointer = start_pointer
    while item_pointer != -1:
        print(linked_list[item_pointer].data)
        item_pointer = linked_list[item_pointer].nextNode

def addNodeUs(linked_list, empty_list):
    data = int(input("Enter value: "))
    if empty_list < 0 or empty_list > 9:
        print("Queue is full!")
        return False
    else:
        linked_list[empty_list].data = data
        item_pointer = 0
        while item_pointer != -1:
            item_pointer = linked_list[item_pointer].nextNode
        linked_list[item_pointer].nextNode = empty_list
        while linked_list[empty_list].data != 0:
            empty_list = linked_list[empty_list].nextNode
        outputNodes(linked_list, startPointer)
        return True

def addNodeMS(linkedList, currentPointer, emptyList):
    dataToAdd = input("Enter the data to add")
    if emptyList <0 or emptyList > 9:
        return False
    else:
        newNode = Node(int(dataToAdd), -1)
        linkedList[emptyList] = (newNode)
        previousPointer = 0
        while(currentPointer != -1):
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        return True

# addNodeMS(linked_list, emptyList)
# addNodeUs(linked_list, emptyList, 12)
# outputNodes(linked_list, startPointer)
# print(linked_list[5].data)

def main():
    outputNodes(linked_list, startPointer)
    result = addNodeMS(linked_list, startPointer, emptyList)
    if result:
        print("Successfully added!")
    else:
        print("Successfully failed!")
    outputNodes(linked_list, startPointer)

main()