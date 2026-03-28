n = int(input())
if not (2 <= n <= 5):
    print("Limit error")

students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([s[1] for s in students]))
second_lowest = scores[1]

names = sorted([s[0] for s in students if s[1] == second_lowest])
for name in names:
    print(name)