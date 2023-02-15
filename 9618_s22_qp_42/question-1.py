stack_data = [0 for i in range(0, 10)]
stack_pointer = 0

def output_values():
    [print(stack_data[i], end=" ") for i in range(0, len(stack_data))]

def push(data):
    global stack_data, stack_pointer
    if stack_pointer == len(stack_data):
        return False
    else:
        stack_data[stack_pointer] = data
        stack_pointer += 1
        return True

def pop():
    global stack_data, stack_pointer
    if stack_pointer == 0:
        return -1
    else:
        data = stack_data[stack_pointer - 1]
        stack_data[stack_pointer - 1] = 0
        stack_pointer -= 1
        return data

def main():
    for i in range(0, 11):
        user_input = int(input("Please enter a number: "))
        is_added = push(user_input)
        message = f"{user_input} has been added to the stack!" if is_added else f"{user_input} hasn't been added to the stack!"
        print(message)
    pop()
    pop()
    output_values()

main()