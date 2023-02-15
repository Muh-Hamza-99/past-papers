# array = [14, 21, 27, 41, 43, 45, 46, 57, 70]

# def binary_search(num_to_find):
#     upper_bound = len(array) - 1
#     lower_bound = 0
#     found = False
#     position = -1
#     while not found and (upper_bound >= lower_bound):
#         i = int((upper_bound + lower_bound) // 2)
#         if array[i] == num_to_find:
#             found = True
#             position = i
#         if array[i] > num_to_find:
#             upper_bound = i - 1
#         if array[i] < num_to_find:
#             lower_bound = i + 1
#     return position

# print(binary_search(57))

array = [14, 21, 27, 41, 43, 45, 46, 57, 70]

def binary_search(num_to_find) -> bool:
    lower_bound = 0
    upper_bound = len(array) - 1
    while upper_bound > lower_bound:
        i = ((lower_bound + upper_bound) // 2)
        if array[i] > num_to_find:
            upper_bound = i - 1
        elif array[i] < num_to_find:
            lower_bound = i + 1
        else:
            return True
    return False

print(binary_search(27))