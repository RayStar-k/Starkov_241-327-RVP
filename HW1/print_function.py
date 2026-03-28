n = int(input())
if not (1 <= n <= 20):
    print("Limit error")

for i in range(1, n + 1):
    print(i, end='')