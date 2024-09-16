import sys

sys.setrecursionlimit(10 ** 6)

def ft_dfs(cx, cy):
    global visited

    dx = (1, -1, 0, 0, -1, -1, 1, 1)
    dy = (0, 0, 1, -1, -1, 1, -1, 1)

    for i in range(8):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < N and 0 <= ny < M and \
            grid[nx][ny] == 1 and (nx, ny) not in visited:
            visited.add((nx, ny))
            ft_dfs(nx, ny)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = set()
cnt = 0
for idx in range(N):
    for jdx in range(M):
        if grid[idx][jdx] == 1 and (idx, jdx) not in visited:
            cnt += 1
            ft_dfs(idx, jdx)
print(cnt)