queue_array = ["" for i in range(10)]
head_pointer = 0
tail_pointer = 0
queue_length = 0

def enqueue(data):
    global queue_array, tail_pointer, queue_length
    if queue_length == len(queue_array):
        return False
    queue_array[tail_pointer] = data
    if tail_pointer >= 9:
        tail_pointer = 0
    else:
        tail_pointer += 1
    queue_length += 1
    return True

def dequeue():
    global queue_array, head_pointer, queue_length
    if queue_length == 0:
        return False
    item = queue_array[head_pointer]
    queue_array[head_pointer] = ""
    if head_pointer >= 9:
        head_pointer = 0
    else:
        head_pointer += 1
    queue_length += 1
    return item

def main():
    for i in range(0, 11):
        user_input = input("Please enter a string: ")
        is_added = enqueue(user_input)
        message = "Successfully added!" if is_added else "Queue is full!"
        print(message)
    print(f"Item removed: {dequeue()}")
    print(f"Item removed: {dequeue()}")

main()