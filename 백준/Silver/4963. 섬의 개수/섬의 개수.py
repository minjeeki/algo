from collections import deque

dx = (1, -1, 0, 0, -1, -1, 1, 1)
dy = (0, 0, 1, -1, -1, 1, -1, 1)

def ft_bfs():
    global deq, visited

    while deq:
        cx, cy = deq.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w and \
                matrix[nx][ny] == 1 and (nx, ny) not in visited:
                deq.append((nx, ny))
                visited.add((nx, ny))

w, h = map(int, input().split())
while w != 0 and h != 0:
    matrix = [list(map(int, input().split())) for _ in range(h)]
    cnt_island = 0
    visited = set()
    deq = deque()
    for idx in range(h):
        for jdx in range(w):
            if matrix[idx][jdx] == 1 and (idx, jdx) not in visited:
                cnt_island += 1
                deq.append((idx, jdx))
                visited.add((idx, jdx))
                ft_bfs()
    print(cnt_island)
    w, h = map(int, input().split())