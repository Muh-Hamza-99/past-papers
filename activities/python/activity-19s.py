def fibonacci(num):
    if num == 0:
        print("Incorrect input!")
        return -1
    elif num == 1:
        answer = 0
    elif num == 2:
        answer = 1
    else:
        answer = fibonacci(num - 1) + fibonacci(num - 2)
    return answer

print(fibonacci(6))

