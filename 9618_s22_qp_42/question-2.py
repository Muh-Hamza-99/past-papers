from random import randint

array_2d = [[randint(1, 100) for i in range(10)] for i in range(0, 10)]

def bubble_sort():
    array_length = 10
    for x in range(0, array_length):
        for y in range(0, array_length - 1):
            for z in range(0, array_length - y - 1):
                if array_2d[x][z] > array_2d[x][z + 1]:
                    temp_value = array_2d[x][z]
                    array_2d[x][z] = array_2d[x][z + 1]
                    array_2d[x][z + 1] = temp_value

def output_2d_array():
    for i in range(0, len(array_2d)):
        row = ""
        for j in range(0, len(array_2d[i])):
            character = f"{array_2d[i][j]}"
            character += "  " if len(character) == 1 else " "
            row += character
        print(row)

def binary_search(search_array, lower, upper, search_value):
    if upper >= lower:
        mid = (lower + (upper - 1)) // 2
        if search_array[0][mid] == search_value:
            return mid
        elif search_array[0][mid] > search_value:
            return binary_search(search_array, lower, mid - 1, search_value)
        elif search_array[0][mid] < search_value:
            return binary_search(search_array, mid + 1, upper, search_value)
    return -1

def main():
    print("2D Array Before Sorting:")
    output_2d_array()
    bubble_sort()
    print("\n2D Array After Sorting:")
    output_2d_array()
    for i in range(0, 2):
        num_to_find = int(input("Please enter a number to find: "))
        index = binary_search(array_2d, 0, 10, num_to_find)
        if index == -1:
            print("Element not found!")
        else:
            print(f"Element found at index {index}.")

main()