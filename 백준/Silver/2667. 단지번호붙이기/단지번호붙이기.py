from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def ft_bfs(cx, cy, cnt_danji):
    global cur_cnt

    deq = deque()
    deq.append((cx, cy))
    matrix[cx][cy] = cnt_danji
    while deq:
        cx, cy = deq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == '1':
                matrix[nx][ny] = cnt_danji
                deq.append((nx, ny))
                cur_cnt += 1

N = int(input())

matrix = [list(input()) for _ in range(N)]
danji = []
cnt_danji = 1
for idx in range(N):
    for jdx in range(N):
        if matrix[idx][jdx] == '1':
            cur_cnt = 1
            ft_bfs(idx, jdx, cnt_danji)
            danji.append(cur_cnt)
            cnt_danji += 1
danji.sort()
print(len(danji), *danji, sep='\n')