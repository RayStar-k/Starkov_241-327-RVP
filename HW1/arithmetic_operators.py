a = int(input())
b = int(input())

if not (1 <= a <= 10**10 and 1 <= b <= 10**10):
    print("Limit error")

print(a + b)
print(a - b)
print(a * b)