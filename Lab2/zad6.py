def fibonacci_generator(n: int):
    num1 = 0
    num2 = 1
    next_num = num2
    count = 1

    fib = []

    while count <= n:
        fib.append(next_num)
        count += 1
        num1, num2 = num2, next_num
        next_num = num1 + num2

    return fib

print(fibonacci_generator(10))