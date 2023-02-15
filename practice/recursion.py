def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def compound_interest(principal, rate, years):
    if years == 0:
        total = principal
    else:
        total = compound_interest(principal * rate, rate, years - 1)
    return total

def fibonacci(number):
    if number == 0:
        print("Incorrect input!")
        return -1
    elif number == 1:
        answer = 0
    elif number == 2:
        answer = 1
    else:
        answer = fibonacci(number - 1) + fibonacci(number - 2)
    return answer