queue = [None for i in range(0, 10)]
front_pointer = 0
rear_pointer = -1
queue_length = 0

def enqueue(data):
    global rear_pointer, queue_length
    if queue_length < len(queue):
        if rear_pointer < len(queue) - 1:
            rear_pointer += 1
        else:
            rear_pointer = 0
        queue_length += 1
        queue[rear_pointer] = data
        print(queue)
    else: 
        print("Queue is full!")

def dequeue():
    global front_pointer, queue_length
    if queue_length >= 0:
        queue[front_pointer] = None
        if front_pointer == len(queue) - 1:
            front_pointer = 0
        else: 
            front_pointer += 1
        queue_length -= 1
        print(queue)
    else:
        print("Queue is empty!")

enqueue(6)
enqueue(5)
enqueue(7)
dequeue()