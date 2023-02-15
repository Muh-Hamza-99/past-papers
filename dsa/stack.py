stack = [None for i in range(0, 10)]
base_pointer = 0
top_pointer = -1

def push(data):
    global top_pointer
    if top_pointer >= len(stack) - 1:
        print("Stack is full!")
    else:
        top_pointer += 1
        stack[top_pointer] = data
        print(stack)

def pop():
    global top_pointer
    if top_pointer == -1:
        print("Stack is empty!")
    else:
        stack[top_pointer] = None
        top_pointer -= 1
        print(stack)

push(5)
push(10)
push(15)
push(20)
push(30)
push(30)
push(30)
push(30)
push(30)
push(30)
push(30)