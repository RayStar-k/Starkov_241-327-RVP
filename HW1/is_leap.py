def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

year = int(input())
if not (1900 <= year <= 10**5):
    print("Limit error")

print(is_leap(year))