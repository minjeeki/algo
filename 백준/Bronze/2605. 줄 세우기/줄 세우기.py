N = int(input())
go_front = list(map(int, input().split()))
line = [i for i in range(1, N+1)]
for idx in range(len(line)):
    if go_front[idx] != 0:
        idx_move = idx - go_front[idx]
        line = line[:idx_move] + [line[idx]] + line[idx_move:idx] + line[idx+1:]
print(*line)