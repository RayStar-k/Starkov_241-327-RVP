s = input()
if not (0 < len(s) <= 1000):
    print("Limit error")

result = ""
for char in s:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(result)