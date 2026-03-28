def compute_average_scores(scores):
    n = len(scores[0])
    averages = []
    for i in range(n):
        total = sum(score[i] for score in scores)
        avg = total / len(scores)
        averages.append(avg)
    return tuple(averages)

if __name__ == '__main__':
    n, x = map(int, input().split())

    # Проверка ограничений: 0 < N ≤ 100, 0 < X ≤ 100
    if not ((0 < n <= 100) and (0 < x <= 100)):
        print("Limit error")
    else:
        scores = []
        for _ in range(x):
            scores.append(tuple(map(float, input().split())))

        averages = compute_average_scores(scores)
        for avg in averages:
            print(f"{avg:.1f}")
