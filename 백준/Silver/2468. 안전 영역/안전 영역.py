from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def ft_bfs(cur_water):
    cnt_section = 0
    visited = set()
    for idx in range(N):
        for jdx in range(N):
            if matrix[idx][jdx] > cur_water and (idx, jdx) not in visited:
                visited.add((idx, jdx))
                cnt_section += 1
                deq = deque()
                deq.append((idx, jdx))
                while deq:
                    cx, cy = deq.popleft()
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if 0 <= nx < N and 0 <= ny < N and \
                            matrix[nx][ny] > cur_water and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            deq.append((nx, ny))
    return cnt_section


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
max_water = max(max(line) for line in matrix)
max_section = 0
# cur_water을 1부터 max_water까지 증가시키기
for cur_water in range(max_water):
    max_section = max(ft_bfs(cur_water), max_section)
print(max_section)