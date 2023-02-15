my_linked_list = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
my_linked_list_pointers = [-1, 0, 1, 2, 3, 6, 7, 8, 9, 10, 11, -1]
start_pointer = 4
heap_start_pointer = start_pointer + 1
NULL_POINTER = -1

def find_item(item):
    found = False
    item_pointer = start_pointer
    while item_pointer != NULL_POINTER and not found:
        if my_linked_list[item_pointer] == item:
            found = True
        else:
            item_pointer = my_linked_list_pointers[item_pointer]
    return item_pointer

def insert_item(item):
    global start_pointer, heap_start_pointer
    if heap_start_pointer != NULL_POINTER:
        temporary_pointer = start_pointer
        start_pointer = heap_start_pointer
        heap_start_pointer = my_linked_list_pointers[heap_start_pointer]
        my_linked_list[start_pointer] = item
        my_linked_list_pointers[start_pointer] = temporary_pointer
        print(my_linked_list)
        print(my_linked_list_pointers)

def delete_item(item):
    global start_pointer, heap_start_pointer
    if start_pointer != NULL_POINTER:
        index = start_pointer
        old_index = 0
        while my_linked_list[index] != item and index != NULL_POINTER:
            old_index = index
            index = my_linked_list_pointers[index]
        if index != NULL_POINTER:
            my_linked_list[index] = None
            temporary_pointer = my_linked_list_pointers[index]
            my_linked_list_pointers[index] = heap_start_pointer
            heap_start_pointer = index
            my_linked_list_pointers[old_index] = temporary_pointer
            print(my_linked_list)
            print(my_linked_list_pointers)

delete_item(16)