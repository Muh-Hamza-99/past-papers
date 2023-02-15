stack = [None for i in range(0, 10)]
base_pointer = 0
top_pointer = -1

def push(item): 
    global top_pointer
    if top_pointer < len(stack) - 1:
        top_pointer += 1
        stack[top_pointer] = item
        print(stack)
    else: 
        print("Stack is full!")

def pop():
    global top_pointer
    if top_pointer != base_pointer - 1:
        stack[top_pointer] = None
        top_pointer -= 1
        print(stack)
    else: 
        print("Stack is empty!")

push(7)
push(32)
pop()
pop()
pop()
test_set = [i + 1 for i in range(0, 10)]
for i in range(0, len(test_set)):
    push(test_set[i])
push(11)