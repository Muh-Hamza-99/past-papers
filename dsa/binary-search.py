array = [14, 21, 27, 41, 43, 45, 46, 57, 70]

def binary_search(array, data):
    found = False
    upper_bound = len(array) - 1
    lower_bound = 0
    position = -1
    while not found and (upper_bound >= lower_bound):
        i = (upper_bound + lower_bound) // 2
        if array[i] == data:
            found = True
            position = i
        if array[i] > data:
            upper_bound -= 1
        if array[i] < data:
            lower_bound += 1
    return position

print(binary_search(array, 70))