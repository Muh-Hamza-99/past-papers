queue_data = ["" for i in range(0, 20)]
start_pointer = 0
end_pointer = -1
queue_length = 0

def enqueue(data):
    global queue_data, end_pointer, queue_length
    if queue_length < len(queue_data):
        if end_pointer < len(queue_data) - 1:
            end_pointer += 1
        else:
            end_pointer = 0
        queue_length += 1
        queue_data[end_pointer] = data
        return True
    else:
        return False

def read_file():
    input_filename = input("Please enter the name of the file your want to read: ")
    try:
        file = open(f"{input_filename}.txt", "r")
        lines = file.readlines()
        for i in range(0, len(lines)):
            data = lines[i].replace("\n", "").strip()
            added_to_queue = enqueue(data)
            if not added_to_queue:
                return 2
        return 1
    except IOError:
        return -1

def dequeue():
    global queue_data, start_pointer, queue_length
    if queue_length > 1:
        data = queue_data[start_pointer]
        if start_pointer < len(queue_data):
            start_pointer += 1
        else:
            start_pointer = 0
        queue_length -= 1
        return data
    else:
        return "No items!"

def remove():
    dequeued_data = []
    for i in range(0, 2):
        data = dequeue()
        if data == "No items!":
            print(data)
            return
        else:
            dequeued_data.append(data)
    return " ".join(dequeued_data)

def main():
    result = read_file()
    if result == 1:
        print("All file data has been successfully inserted in the queue!")
    elif result == 2:
        print("All file data hasn't been successfully inserted in queue as it is full!")
    elif result == -1:
        print("Input filename can't be found!")
main()