N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    total = 0
    for idx in range(i - 1, x):
        for jdx in range(j - 1, y):
            total += matrix[idx][jdx]
    print(total)