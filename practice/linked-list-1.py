# linked_list = [None for i in range(0, 10)]
# linked_list_pointers = [i+1 for i in range(0, 10)]
# linked_list_pointers[-1] = -1
# start_pointer = -1
# heap_start_pointer = 0
# NULL_POINTER = -1

# def search(data) -> bool:
#     global start_pointer
#     while start_pointer != NULL_POINTER:
#         if linked_list[start_pointer] == data:
#             return True
#         else:
#             start_pointer = linked_list_pointers[start_pointer]
#     return False

# def insert(data):
#     global start_pointer, heap_start_pointer
#     if heap_start_pointer != NULL_POINTER:
#         if start_pointer == -1:
#             linked_list[0] = data
#             linked_list_pointers[0] = -1
#             start_pointer, heap_start_pointer = 0, 1
#         else:
#             temporary_pointer = start_pointer
#             start_pointer = heap_start_pointer
#             heap_start_pointer = linked_list_pointers[heap_start_pointer]
#             linked_list[start_pointer] = data
#             linked_list_pointers[start_pointer] = temporary_pointer
#     else:
#         print("Linked list is full!")

# def remove(data):
#     global start_pointer, heap_start_pointer
#     if start_pointer != NULL_POINTER:
#         index = start_pointer
#         old_index = 0
#         while linked_list[index] != data and index != NULL_POINTER:
#             old_index = index
#             index = linked_list_pointers[index]
#         if index != NULL_POINTER:
#             linked_list[index] = None
#             temporary_pointer = linked_list_pointers[index]
#             linked_list_pointers[index] = heap_start_pointer
#             heap_start_pointer = index
#             linked_list_pointers[old_index] = temporary_pointer
#         else: 
#             print(f"{data} not found in list!")
#     else:
#         print("Linked list is empty!")