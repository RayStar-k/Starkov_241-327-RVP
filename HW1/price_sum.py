with open('products.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

adult_sum = 0
pensioner_sum = 0
child_sum = 0

for i in range(1, len(lines)):
    line = lines[i].strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) >= 4:
        adult_sum += float(parts[1])
        pensioner_sum += float(parts[2])
        child_sum += float(parts[3])

print(f"{adult_sum:.2f} {pensioner_sum:.2f} {child_sum:.2f}")