n = int(input())
passengers = []
for _ in range(n):
    entry, exit = map(int, input().split())
    passengers.append((entry, exit))
t = int(input())

count = 0
for entry, exit in passengers:
    if entry <= t <= exit:
        count += 1

print(count)