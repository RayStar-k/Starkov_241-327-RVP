n, m = map(int, input().split())
if not (1 <= n <= 10**5 and 1 <= m <= 10**5):
    print("Limit error")

arr = list(map(int, input().split()))
if not all(1 <= i <= 10**9 for i in arr):
    print("Limit error")

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)