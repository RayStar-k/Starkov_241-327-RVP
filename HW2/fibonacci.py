cube = lambda x: x**3

def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

if __name__ == '__main__':
    n = int(input())

    # Проверка ограничений: 1 ≤ n ≤ 15
    if not (1 <= n <= 15):
        print("Limit error")
    else:
        print(list(map(cube, fibonacci(n))))
