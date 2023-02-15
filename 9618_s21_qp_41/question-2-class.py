array_data = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linear_search(integer):
    for i in range(0, len(array_data)):
        if array_data[i] == integer:
            return True
    return 
    
def bubble_sort():
    length = len(array_data)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array_data[j] < array_data[j + 1]:
                array_data[j], array_data[j + 1] = array_data[j + 1], array_data[j]
    print(array_data)

def main():
    input_integer = int(input("Please enter an integer: "))
    found = linear_search(input_integer)
    message = f"{input_integer} found!" if found else f"{input_integer} not found!"
    print(message)

bubble_sort()