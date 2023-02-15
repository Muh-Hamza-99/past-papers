def factorial_recursion(num):
    if num == 0:
        answer = 1
    else: 
        answer = num * factorial_recursion(num - 1)
    return answer

def factorial_iterative(num):
    answer = 1
    for i in range(1, num + 1):
        answer *= i
    return answer

print(factorial_recursion(5))
print(factorial_iterative(5))