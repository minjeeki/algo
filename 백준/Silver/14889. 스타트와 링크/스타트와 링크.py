from itertools import combinations

n = int(input())

stat = [list(map(int, input().split())) for _ in range(n)]

stat_sum = sorted([sum(i)+sum(j) for i, j in zip(stat, zip(*stat))])
all_stat = sum(stat_sum) // 2

result = 10**9

for c in combinations(stat_sum, n//2):
    result = min(result, abs(all_stat - sum(c)))

print(result)