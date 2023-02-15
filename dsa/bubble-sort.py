array = [70, 46, 43, 27, 57, 41, 45, 21, 14]

def bubble_sort(array):
    swap = True
    top = len(array)
    while (swap) and (top > 0):
        swap = False
        for i in range(top - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        top -= 1
    print(array)

bubble_sort(array)