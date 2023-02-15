array_nodes = [[0 for j in range(0, 3)] for i in range(0, 20)]
root_pointer = -1
free_node = 0

def add_node(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the Data"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1: # Add to start
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")

def print_all():
    for i in range(0, len(array_nodes)):
        print(array_nodes[i][0], array_nodes[i][1], array_nodes[i][2])

def main():
    for i in range(0, 9):
        add_node(array_nodes, root_pointer, free_node)
    print_all()

main()