n, m = map(int, input().split())
items = []
for _ in range(m):
    parts = input().split()
    name = parts[0]
    weight = int(parts[1])
    cost = int(parts[2])
    items.append((name, weight, cost, cost / weight))

items.sort(key=lambda x: x[3], reverse=True)

capacity = n
result = []
for name, weight, cost, ratio in items:
    if capacity >= weight:
        result.append((name, weight, cost))
        capacity -= weight
    elif capacity > 0:
        fraction = capacity / weight
        result.append((name, round(capacity, 2), round(cost * fraction, 2)))
        capacity = 0
        break

for name, weight, cost in result:
    print(f"{name} {weight} {cost}")