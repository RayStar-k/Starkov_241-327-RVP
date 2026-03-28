n = int(input())
if not (1 <= n <= 20):
    print("Limit error")

for i in range(n):
    print(i ** 2)