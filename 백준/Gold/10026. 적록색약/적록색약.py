from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

N = int(input())
grid = [list(input()) for _ in range(N)]

visited_normal = set()
deq_normal = deque()
cnt_normal = 0
for ni in range(N):
    for nj in range(N):
        if (ni, nj) not in visited_normal:
            cnt_normal += 1
            deq_normal.append((ni, nj))
            check = grid[ni][nj]
            while deq_normal:
                cx, cy = deq_normal.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == check and (nx, ny) not in visited_normal:
                        visited_normal.add((nx, ny))
                        deq_normal.append((nx, ny))

visited_blind = set()
deq_blind = deque()
cnt_blind = 0
for bi in range(N):
    for bj in range(N):
        if (bi, bj) not in visited_blind:
            cnt_blind += 1
            deq_blind.append((bi, bj))
            if grid[bi][bj] == 'R' or grid[bi][bj] == 'G':
                check = {'R', 'G'}
            else:
                check = {'B'}
            while deq_blind:
                cx, cy = deq_blind.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] in check and (nx, ny) not in visited_blind:
                        visited_blind.add((nx, ny))
                        deq_blind.append((nx, ny))
print(cnt_normal, cnt_blind)