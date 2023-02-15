array = [70, 46, 43, 27, 57, 41, 45, 21, 14]

def linear_search(array, data):
    for i in range(0, len(array)):
        if array[i] == data:
            return i
    return -1

print(linear_search(array, 50))