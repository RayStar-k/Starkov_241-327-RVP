def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)

def fact_it(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    import timeit
    n = 10

    # Проверка ограничений: 1 ≤ n ≤ 10^5
    if not (1 <= n <= 10**5):
        print("Limit error")
    else:
        rec_time = timeit.timeit(lambda: fact_rec(n), number=10000)
        it_time = timeit.timeit(lambda: fact_it(n), number=10000)
        print(f"Recursive: {rec_time:.6f}s, Iterative: {it_time:.6f}s")
