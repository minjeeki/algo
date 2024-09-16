subjects = [(idx, int(input())) for idx in range(1, 9)]
high_scores = sorted((sorted(subjects, key = lambda x: -x[1]))[:5], key = lambda x: x[0])
print(sum(item[1] for item in high_scores))
print(*list(zip(*high_scores))[0])