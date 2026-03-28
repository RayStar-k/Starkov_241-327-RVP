import re

with open('example.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = re.findall(r'\b\w+\b', text)
if not words:
    exit()

max_length = max(len(word) for word in words)
max_words = []
seen = set()
for word in words:
    if len(word) == max_length and word not in seen:
        max_words.append(word)
        seen.add(word)

for word in max_words:
    print(word)