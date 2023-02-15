def factorial(num):
    if num == 0:
        answer = 1
    else: 
        answer = num * factorial(num - 1)
    return answer

print(factorial(0))
print(factorial(5))