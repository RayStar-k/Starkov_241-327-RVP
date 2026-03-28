import random

def circle_square_mk(r, n):
    inside = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            inside += 1
    return (inside / n) * (2 * r) ** 2

if __name__ == '__main__':
    import math
    r = 5
    for n in [100, 1000, 10000, 100000]:
        mk_area = circle_square_mk(r, n)
        real_area = math.pi * r ** 2
        error = abs(mk_area - real_area) / real_area * 100
        print(f"n={n}: MC={mk_area:.2f}, Real={real_area:.2f}, Error={error:.2f}%")
