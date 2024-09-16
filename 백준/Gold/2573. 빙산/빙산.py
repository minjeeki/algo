from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def ft_melting():
    new_grid = [[0] * M for _ in range(N)]
    for idx in range(N):
        for jdx in range(M):
            if grid[idx][jdx] > 0:
                melting = 0
                for i in range(4):
                    near_x = idx + dx[i]
                    near_y = jdx + dy[i]
                    if 0 <= near_x < N and 0 <= near_y < M and grid[near_x][near_y] == 0:
                        melting += 1
                new_grid[idx][jdx] = max(grid[idx][jdx] - melting, 0)
    return new_grid

def ft_bfs():
    cnt_iceberg = 0
    visited = set()
    for idx in range(N):
        for jdx in range(M):
            if grid[idx][jdx] > 0 and (idx, jdx) not in visited:
                cnt_iceberg += 1
                if cnt_iceberg > 1:
                    return 2
                deq = deque()
                deq.append((idx, jdx))
                while deq:
                    cx, cy = deq.popleft()
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] > 0 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            deq.append((nx, ny))
    return cnt_iceberg

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
max_height = max(max(row) for row in grid)
year = 0
cnt_iceberg = 1
while cnt_iceberg == 1:
    # 빙하 녹이기
    year += 1
    grid = ft_melting()
    # 빙하 덩어리 개수 세기
    cnt_iceberg = ft_bfs()
    if cnt_iceberg > 1:
        print(year)
        break
else:
    print(0)