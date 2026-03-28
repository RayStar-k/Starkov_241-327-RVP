import operator

def person_lister(f):
    def inner(people):
        people_sorted = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in people_sorted]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    n = int(input())

    # Проверка ограничений: 1 ≤ N ≤ 10
    if not (1 <= n <= 10):
        print("Limit error")
    else:
        people = [input().split() for i in range(n)]
        print(*name_format(people), sep='\n')
