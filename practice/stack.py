# stack = [None for i in range(0, 10)]
# top_pointer = -1
# base_pointer = 0

# def push(data):
#     global top_pointer, stack
#     if top_pointer < len(stack) - 1:
#         top_pointer += 1
#         stack[top_pointer] = data
#     else:
#         print("Stack is full!")

# def pop():
#     global top_pointer, base_pointer, stack
#     if top_pointer != base_pointer - 1:
#         stack[top_pointer] = None
#         top_pointer -= 1
#     else:
#         print("Stack is empty!")

stack = [None for i in range(0, 10)]
base_pointer = 0
top_pointer = -1

def push(data):
    global top_pointer
    if top_pointer < len(stack) - 1:
        top_pointer += 1
        stack[top_pointer] = data
    else:
        print("Stack is full!")

def pop():
    global top_pointer
    if top_pointer > base_pointer - 1:
        stack[top_pointer] = None
        top_pointer -= 1
    else:
        print("Stack is empty!")