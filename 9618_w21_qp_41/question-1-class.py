def unknown(x, y):
    if x < y:
        print(x + y)
        return (unknown(x + 1, y)) * 2
    elif x == y:
        return 1
    else:
        print(x + y)
        return int(unknown(x - 1, y) / 2)

def iterative_unknown(x, y):
    total = 1
    while x != y:
        print(x + y)
        if x < y:
            x += 1
            total = total * 2
        else:
            x -= 1
            total = int(total / 2)
    return total

def main():
    parameters = [[10, 15], [10, 10], [15, 10]]
    for i in range(0, len(parameters)):
        x, y = parameters[i][0], parameters[i][1]
        print(f"x = {x} y = {y}")
        result = iterative_unknown(x, y)
        print(f"{result}\n")

main()