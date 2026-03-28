def process_list(arr):
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3

if __name__ == '__main__':
    import timeit
    arr = list(range(1, 11))

    # Проверка ограничений: 1 ≤ len(arr) ≤ 10^3
    if not (1 <= len(arr) <= 10**3):
        print("Limit error")
    else:
        lc_time = timeit.timeit(lambda: process_list(arr), number=100000)
        gen_time = timeit.timeit(lambda: list(process_list_gen(arr)), number=100000)
        print(f"List comprehension: {lc_time:.6f}s, Generator: {gen_time:.6f}s")
