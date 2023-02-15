array = [70, 46, 43, 27, 57, 41, 45, 21, 14]

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        place = i - 1
        if array[place] > key:
            while array[place] > key and place >= 0:
                array[place], array[place + 1] = array[place + 1], array[place]
                place -= 1
            array[place + 1] = key

insertion_sort(array)
print(array)